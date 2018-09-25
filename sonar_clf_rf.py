from csv import reader
from math import sqrt
from random import randrange, seed


def load_csv(filename):
    """This method loads a csv file"""
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)

    return dataset


def str_column_to_float(dataset, column):
    """This method converts a string column to float"""
    for row in dataset:
        row[column] = float(row[column].strip())


def str_columm_to_int(dataset, column):
    """This method converts a string column to int"""
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()

    for i, value in enumerate(unique):
        lookup[value] = i

    for row in dataset:
        row[column] = lookup[row[column]]

    return lookup


def cross_validation_split(dataset, k_folds):
    """This method splits a dataset into k folds"""
    dataset_split = list()
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / k_folds)

    for i in range(k_folds):
        fold = list()
        while(len(fold) < fold_size):
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)

    return dataset_split


def accuracy_score(actual, predicted):
    """This method predicts the accuracy percentage"""
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1

    return correct / float(len(actual)) * 100.0


def evaluate_algorithm(dataset, algorithm, k_folds, *args):
    """This method evaluates the algorithm using a cross validation split"""
    folds = cross_validation_split(dataset, k_folds)
    scores = list()

    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])

        test_set = list()

        for row in fold:
            row_copy = list(row)
            test_set.append(row_copy)
            row_copy[-1] = None

        predicted = algorithm(train_set, test_set, *args)
        actual = [row[-1] for row in fold]

        accuracy = accuracy_score(actual, predicted)
        scores.append(accuracy)

        return scores


def test_split(index, value, dataset):
    """This method split a dataset based on an attribute and an attribute value"""
    left, right = list(), list()

    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)

    return left, right


def gini_index(groups, classes):
    """This method calculates the gini index for a split dataset"""
    # count all samples at split point
    n_instances = float(sum([len(group) for group in groups]))
    # sum weighted gini index for each group
    gini = 0.0
    for group in groups:
        size = float(len(group))
        # avoid divide ny zero
        if size == 0:
            continue
        score = 0.0
        # score tje group based on the score for each class
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        # weight the group score by its relative size
        gini += (1.0 - score) * (size / n_instances)

    return gini


def get_split(dataset, n_features):
    """This method selects the best split for the dataset"""
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    features = list()

    while len(features) < n_features :
        index = randrange(len(dataset[0]) - 1)
        if index not in features:
            features.append(index)

    for index in features:
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)

            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups

    return {'index':b_index, 'value':b_value, 'groups':b_groups}


def to_terminal(group):
    """Create a terminal node value"""
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)


def split(node, max_depth, min_size, n_features, depth):
    left, right = node['groups']
    del node['groups']

    # check for a no split
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)

    # check for max_depth
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return

    # process left child
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left, n_features)
        split(node['left'], max_depth, min_size, n_features, depth+1)

    # process right child
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right, n_features)
        split(node['right'], max_depth, min_size, n_features, depth+1)


def build_tree(train, max_depth, min_size, n_features):
    """This method builds a decision tree"""
    root = get_split(train, n_features)
    split(root, max_depth, min_size, n_features, 1)
    return root


def predict(node, row):
    """This method makes a prediction with a decision tree"""
    if row[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']


def subsample(dataset, ratio):
    """This method creates a random subsample from the dataset with replacement"""
    sample = list()
    n_sample = round(len(dataset) * ratio)
    while len(sample) < n_sample:
        index = randrange(len(dataset))
        sample.append(dataset[index])
    return sample


def bagging_predict(trees, row):
    """This method makes a prediction a list of bagged trees"""
    predictions = [predict(tree, row) for tree in trees]
    return max(set(predictions), key=predictions.count)


def random_forest(train, test, max_depth, min_size, sample_size, n_trees, n_features):
    """Random Forest Algorithm"""
    trees = list()
    for i in range(n_trees):
        sample = subsample(train, sample_size)
        tree = build_tree(sample, max_depth, min_size, n_features)
        trees.append(tree)
    predictions = [bagging_predict(trees, row) for row in test]
    return predictions


"""Test run the algorithm"""
seed(2)
# load and prepare the data
filename = "/home/amogh/PycharmProjects/deeplearning/indie_projects/sonar_data.csv"
dataset = load_csv(filename)
# convert string attributes to integers
for i in range(0, len(dataset[0]) - 1):
    str_column_to_float(dataset, i)
# convert class columns to integers
str_columm_to_int(dataset, len(dataset[0]) - 1)

# evaluate algorithm
k_folds = 5
max_depth = 10
min_size = 1
sample_size = 1.0
n_features = int(sqrt(len(dataset[0]) - 1))

for n_trees in [1, 5, 10]:
    scores = evaluate_algorithm(dataset, random_forest, k_folds, max_depth, min_size, sample_size, n_trees, n_features)
    print("Trees: %d" % n_trees)
    print("Scores: %d" % scores)
    print("Mean Accuracy: %.3f%%" % (sum(scores) / float(len(scores))))
