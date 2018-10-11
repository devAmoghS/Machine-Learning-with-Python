import random
from helpers.gradient_descent import minimize_stochastic
from simple_linear_regression.data import num_friends_good, daily_minutes_good
from simple_linear_regression.utils import least_squares_fit, r_squared, squared_error, squared_error_gradient

if __name__ == '__main__':

    alpha, beta = least_squares_fit(num_friends_good, daily_minutes_good)
    print("alpha", alpha)
    print("beta", beta)

    print("r-squared", r_squared(alpha, beta, num_friends_good, daily_minutes_good))

    print()

    print("gradient descent:")
    # choose random value to start
    random.seed(0)
    theta = [random.random(), random.random()]
    alpha, beta = minimize_stochastic(squared_error,
                                      squared_error_gradient,
                                      num_friends_good,
                                      daily_minutes_good,
                                      theta,
                                      0.0001)
    print("alpha", alpha)
    print("beta", beta)
