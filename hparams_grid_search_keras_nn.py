import numpy as np
import pandas as pd
from keras import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

DATA_FILE = ''

feature_cols = ['feat1', 'feat2', 'feat3', 'feat4', 'feat5', 'feat6']
labels = ['y']


def load_data(filepath):
    data = pd.read_csv(filepath)
    return data


def describe_data(data, name):
    print('\nGetting the summary for ' + name + '\n')
    print('Dataset Length:', len(data))
    print('Dataset Shape:', data.shape)
    print(data.columns)
    print(data.dtypes)


def create_model():
    model = Sequential()
    model.add(Dense(12, input_dim=5, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(8, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model


if __name__ == '__main__':

    data_df = load_data(DATA_FILE)

    data_df = data_df.dropna()
    print(data_df.isnull().sum(axis=0))

    X_data = data_df[feature_cols]
    y_data = data_df[['y']]

    # seed for reproducibility
    seed = 7
    np.random.seed(seed=seed)

    # train test split
    X, X_test, y, y_test = train_test_split(X_data, y_data, test_size=.20, random_state=42)

    # train val split
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=.20, random_state=42)

    # summarize the datasets
    describe_data(X_train, name="X_train")
    describe_data(X_val, name="X_val")
    describe_data(X_test, name="X_test")
    describe_data(y_train, name="y_train")
    describe_data(y_val, name="y_val")
    describe_data(y_test, name="y_test")

    # create model
    model = KerasClassifier(build_fn=create_model)

    # hyperparamater optimization
    batch_size = [10, 20, 40, 60, 80, 100]
    epochs = [10, 50, 100]
    learn_rate = [0.001, 0.01, 0.1, 0.2, 0.3]
    momentum = [0.0, 0.2, 0.4, 0.6, 0.8, 0.9]
    weight_constraint = [1, 2, 3, 4, 5]
    dropout_rate = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    neurons = [1, 5, 10, 15, 20, 25, 30]

    param_grid = dict(batch_size=batch_size, epochs=epochs)
    grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1)
    grid_result = grid.fit(X=X_train, y=y_train)

    # summarize results
    print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
    means = grid_result.cv_results_['mean_test_score']
    stds = grid_result.cv_results_['std_test_score']
    params = grid_result.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
        print("%f (%f) with: %r" % (mean, stdev, param))













