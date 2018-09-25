import pandas as pd
import numpy as np
from IPython.display import display
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, roc_curve
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv("/home/amogh/Downloads/Churn.csv")
display(df.head(5))

"""Data Exploration and Cleaning"""
# print("Number of rows: ", df.shape[0])
# counts = df.describe().iloc[0]
# display(pd.DataFrame(counts.tolist(), columns=["Count of values"], index=counts.index.values).transpose)

"""Feature Selection"""
df = df.drop(["Phone", "Area Code", "State"], axis=1)
features = df.drop(["Churn"], axis=1).columns

"""Fitting the model"""
df_train, df_test = train_test_split(df, test_size=0.25)
clf = RandomForestClassifier()
clf.fit(df_train[features], df_train["Churn"])

# Make predictions
preds = clf.predict(df_test[features])
probs = clf.predict_proba(df_test[features])
display(preds)

"""Evaluating the model"""
score = clf.score(df_test[features], df_test["Churn"])
print("Accuracy: ", score)

cf = pd.DataFrame(confusion_matrix(df_test["Churn"], preds), columns=["Predicted False", "Predicted True"], index=["Actual False", "Actual True"])

display(cf)

# Plotting the ROC curve

fpr, tpr, threshold = roc_curve(df_test["Churn"], probs[:, 1])
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

# Feature Importance Plot
fig = plt.figure(figsize=(20, 18))
ax = fig.add_subplot(111)

df_f = pd.DataFrame(clf.feature_importances_, columns=["importance"])
df_f["labels"] = features
df_f.sort_values("importance", inplace=True, ascending=False)
display(df_f.head(5))

index = np.arange(len(clf.feature_importances_))
bar_width = 0.5
rects = plt.barh(index, df_f["importance"], bar_width, alpha=0.4, color='b', label='Main')
plt.yticks(index, df_f["labels"])
plt.show()

df_test["prob_true"] = probs[:, 1]
df_risky = df_test[df_test["prob_true"] > 0.9]
display(df_risky.head(5)[["prob_true"]])
