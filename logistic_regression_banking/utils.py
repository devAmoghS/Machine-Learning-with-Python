import seaborn as sns
import matplotlib.pyplot as plt

plt.rc("font", size=14)
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)


def plot_data(data):
    # barplot for the depencent variable
    sns.countplot(x='y', data=data, palette='hls')
    plt.show()

    # check the missing values
    print(data.isnull().sum())

    # customer distribution plot
    sns.countplot(y='job', data=data)
    plt.show()

    # customer marital status distribution
    sns.countplot(x='marital', data=data)
    plt.show()

    # barplot for credit in default
    sns.countplot(x='default', data=data)
    plt.show()

    # barptot for housing loan
    sns.countplot(x='housing', data=data)
    plt.show()

    # barplot for personal loan
    sns.countplot(x='loan', data=data)
    plt.show()

    # barplot for previous marketing campaign outcome
    sns.countplot(x='poutcome', data=data)
    plt.show()

