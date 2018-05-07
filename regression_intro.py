import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

# Style file for plotting graph
style.use('ggplot')

# Retrieve dataframe from Quandl
df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume',]]
# High Low Change => Volatility of the stock
df['HL_PCT'] =  (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0
# Percentage Change => Volatility change
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

# Modified data frame with important features and labels
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
forecast_col = 'Adj. Close'

# In case, data is missing: replace with threshold value to make it outlier
df.fillna(-99999, inplace=True)

# Predicting 1% (0.01) [1 day into the future]
forecast_out = int(math.ceil(0.01 * len(df)))
print(forecast_out)

# shifting them by 35 days timeframe
df['label'] = df[forecast_col].shift(-forecast_out)

# *** FEATURES & LABELS are obtained ***
# X is the set of features except the label, 1 indicates the column
# ref: stackoverflow.com => ambiguity-in-pandas-dataframe-numpy-array-axis-definition
X = np.array(df.drop(['label'], 1))

# Scaling the features to normalize them between -1 and 1
# done for efficiency and accuracy, but not required
X = preprocessing.scale(X)
# Prediction will be made against X_lately
X_lately = X[-forecast_out:]
X = X[:-forecast_out]
df.dropna(inplace=True)
# y is the label array
y = np.array(df['label'])

# *** CREATING TRAINING TESTING SETS with 20% (0.2) data ***
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

# using two classifiers: LinearRegression(single-threaded) and SVM(default kernel)
clf = LinearRegression()
# clf = svm.SVR()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
# forecast_set will be an array of predicted values for the next 35 days
forecast_set = clf.predict(X_lately)
# print(accuracy)
print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan

# *** DateTime information for our dataframe is obtained ***
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day_in_secs = 86400
next_unix = last_unix + one_day_in_secs

for i in forecast_set:
  next_date = datetime.datetime.fromtimestamp(next_unix)
  next_unix += one_day_in_secs
  # loc is used for indexing
  df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

print(df.tail())

# *** VISUALISATION OF FORECAST ***
df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
