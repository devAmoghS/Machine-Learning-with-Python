from helpers.stats import correlation, standard_deviation, mean, de_mean


def predict(alpha, beta, x_i):
    return beta * x_i + alpha


def error(alpha, beta, x_i, y_i):
    return y_i - predict(alpha, beta, x_i)


def sum_of_squared_errors(alpha, beta, x, y):
    return sum(error(alpha, beta, x_i, y_i) ** 2
               for x_i, y_i in zip(x, y))


def least_squares_fit(x, y):
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta


def total_sum_of_squares(y):
    """The total squared variation of y_i's from their mean"""
    return sum(v ** 2 for v in de_mean(y))


def r_squared(alpha, beta, x, y):
    """the fraction of variation in y captured by the model"""
    return 1 - sum_of_squared_errors(alpha, beta, x, y) / total_sum_of_squares(y)


def squared_error(x_i, y_i, theta):
    alpha, beta = theta
    return error(alpha, beta, x_i, y_i) ** 2


def squared_error_gradient(x_i, y_i, theta):
    alpha, beta = theta
    return [-2 * error(alpha, beta, x_i, y_i),          # alpha partial derivative
            -2 * error(alpha, beta, x_i, y_i) * x_i]    # beta partial derivative



