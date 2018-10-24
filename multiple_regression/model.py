import random

from helpers.linear_algebra import dot
from helpers.stats import median, standard_deviation
from multiple_regression.data import x, daily_minutes_good
from multiple_regression.utils import estimate_beta, multiple_r_squared, bootstrap_statistic, estimate_sample_beta, \
    p_value, estimate_beta_ridge

if __name__ == '__main__':
    random.seed(0)
    beta = estimate_beta(x, daily_minutes_good)  # [30.63, 0.972, -1.868, 0.911]
    print("beta", beta)
    print("r-squared", multiple_r_squared(x, daily_minutes_good, beta))
    print()

    print("digression: the bootstrap")
    # 101 points all very close to 100
    close_to_100 = [99.5 + random.random() for _ in range(101)]

    # 101 points, 50 of them near 0, 50 of them near 200
    far_from_100 = ([99.5 + random.random()] +
                    [random.random() for _ in range(50)] +
                    [200 + random.random() for _ in range(50)])

    print("bootstrap_statistic(close_to_100, median, 100):")
    print(bootstrap_statistic(close_to_100, median, 100))
    print("bootstrap_statistic(far_from_100, median, 100):")
    print(bootstrap_statistic(far_from_100, median, 100))
    print()

    random.seed(0)  # so that you get the same results as me

    bootstrap_betas = bootstrap_statistic(list(zip(x, daily_minutes_good)),
                                          estimate_sample_beta,
                                          100)

    bootstrap_standard_errors = [
        standard_deviation([beta[i] for beta in bootstrap_betas])
        for i in range(4)]

    print("bootstrap standard errors", bootstrap_standard_errors)
    print()

    print("p_value(30.63, 1.174)", p_value(30.63, 1.174))
    print("p_value(0.972, 0.079)", p_value(0.972, 0.079))
    print("p_value(-1.868, 0.131)", p_value(-1.868, 0.131))
    print("p_value(0.911, 0.990)", p_value(0.911, 0.990))
    print()

    print("regularization")

    random.seed(0)
    for alpha in [0.0, 0.01, 0.1, 1, 10]:
        beta = estimate_beta_ridge(x, daily_minutes_good, alpha=alpha)
        print("alpha", alpha)
        print("beta", beta)
        print("dot(beta[1:],beta[1:])", dot(beta[1:], beta[1:]))
        print("r-squared", multiple_r_squared(x, daily_minutes_good, beta))
        print()