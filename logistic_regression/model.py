import random
from functools import partial

from helpers.gradient_descent import maximize_batch, maximize_stochastic
from helpers.linear_algebra import dot
from helpers.machine_learning import train_test_split
from logistic_regression.data import data
from logistic_regression.utils import logistic_log_likelihood, logistic_log_gradient, logistic_log_likelihood_i, \
    logistic_log_gradient_i, logistic
from multiple_regression.utils import estimate_beta
from working_with_data.utils import rescale

if __name__ == '__main__':
    x = [[1] + row[:2] for row in data]  # each element is [1, experience, salary]
    y = [row[2] for row in data]  # each element is paid_account

    print("linear regression:")

    rescaled_x = rescale(x)
    beta = estimate_beta(rescaled_x, y)
    print(beta)

    print("logistic regression:")

    random.seed(0)
    x_train, x_test, y_train, y_test = train_test_split(rescaled_x, y, 0.33)

    # want to maximize log likelihood on the training data
    fn = partial(logistic_log_likelihood, x_train, y_train)
    gradient_fn = partial(logistic_log_gradient, x_train, y_train)

    # pick a random starting point
    beta_0 = [1, 1, 1]

    # and maximize using gradient descent
    beta_hat = maximize_batch(fn, gradient_fn, beta_0)

    print("beta_batch", beta_hat)

    beta_0 = [1, 1, 1]
    beta_hat = maximize_stochastic(logistic_log_likelihood_i,
                                   logistic_log_gradient_i,
                                   x_train, y_train, beta_0)

    print("beta stochastic", beta_hat)

    true_positives = false_positives = true_negatives = false_negatives = 0

    for x_i, y_i in zip(x_test, y_test):
        predict = logistic(dot(beta_hat, x_i))

        if y_i == 1 and predict >= 0.5:  # TP: paid and we predict paid
            true_positives += 1
        elif y_i == 1:  # FN: paid and we predict unpaid
            false_negatives += 1
        elif predict >= 0.5:  # FP: unpaid and we predict paid
            false_positives += 1
        else:  # TN: unpaid and we predict unpaid
            true_negatives += 1

    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)

    print("precision", precision)
    print("recall", recall)