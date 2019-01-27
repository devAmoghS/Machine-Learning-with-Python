import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

plt.rc("font", size=14)
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

if __name__ == '__main__':

    data = pd.read_csv('banking.csv', header=0)
    data = data.dropna()
    print(data.shape)
    print(list(data.columns))

    # plot_data(data)

    # The prediction will be based on the variables selected in plot_data(), all other varaible are dropped

    data.drop(data.columns[[0, 3, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19]], axis=1, inplace=True)

    # print(data.shape)
    # print(list(data.columns))

    # Data preprocessing

    """dummy varaiable are variables with only two values: one or zero."""

    data2 = pd.get_dummies(data, columns=['job', 'marital', 'default', 'housing', 'loan', 'poutcome'])

    # drop the unknown columns
    data2.drop(data2.columns[[12, 16, 18, 21, 24]], axis=1, inplace=True)

    print(data2.columns)

    # plot the correlation between variables
    # sns.heatmap(data2.corr())
    # plt.show()

    # split the data into training and test sets
    X = data2.iloc[:, 1:]
    y = data2.iloc[:, 0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    print(X_train.shape)

    # Logistic Regression Model
    clf = LogisticRegression(random_state=0)
    clf.fit(X_train, y_train)

    # predicting the test results and confusion matrix
    y_pred = clf.predict(X_test)
    confusion_matrix = confusion_matrix(y_test, y_pred)
    print(confusion_matrix)

    print('Accuracy: {:.2f}'.format(clf.score(X_test, y_test)))

    print(classification_report(y_test, y_pred))

    pca = PCA(n_components=2).fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(pca, y, random_state=0)

    plt.figure(dpi=120)
    plt.scatter(pca[y.values == 0, 0], pca[y.values == 0, 1], alpha=0.5, label='YES', s=2, color='navy')
    plt.scatter(pca[y.values == 1, 0], pca[y.values == 1, 1], alpha=0.5, label='NO', s=2, color='darkorange')
    plt.legend()
    plt.title('Bank Marketing Data Set\nFirst Two Principal Components')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.gca().set_aspect('equal')
    plt.show()



