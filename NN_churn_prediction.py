"""Importing the libraries"""
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

"""Loading the data"""
dataset = pd.read_csv("/home/amogh/Downloads/Churn_Modelling.csv")

# filtering features and labels
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

"""Preprocessing the data"""
# encoding the Gender and Geography
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])   # Column 4 [France, Germany, Spain] => [0, 1, 2]
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])   # Column 5 [Male, Female] => [0, 1]

# splitting the data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# scaling features
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

"""Building the neural network"""
# initializing the neural network
model = Sequential()
# input and first hidden layer
model.add(Dense(6, input_dim=10, activation='relu'))
# second hidden layer
model.add(Dense(6, activation='relu'))
# output layer - probability of churning
model.add(Dense(1, activation='sigmoid'))
# compiling the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

"""Running the model on the data"""
# fitting the model
model.fit(X_train, y_train, batch_size=10, epochs=100)

y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5)     # converting probabilities into binary

"""Evaluating the results"""
# generating the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# determining the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

# generating the classification report
cr = classification_report(y_test, y_pred)
print(cr)
