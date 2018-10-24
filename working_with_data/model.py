import csv
from collections import defaultdict
from functools import reduce

import dateutil

from helpers.stats import correlation
from working_with_data.data import X
from working_with_data.utils import parse_rows_with, parse_dict, day_over_day_changes, picker, group_by, random_normal, \
    pluck, scale, rescale, de_mean_matrix, principal_component_analysis, transform_vector

if __name__ == "__main__":

    xs = [random_normal() for _ in range(1000)]
    ys1 = [x + random_normal() / 2 for x in xs]
    ys2 = [-x + random_normal() / 2 for x in xs]

    print("correlation(xs, ys1)", correlation(xs, ys1))
    print("correlation(xs, ys2)", correlation(xs, ys2))

    # safe parsing

    data = []

    with open("comma_delimited_stock_prices.csv", "r", encoding='utf8', newline='') as f:
        reader = csv.reader(f)
        for line in parse_rows_with(reader, [dateutil.parser.parse, None, float]):
            data.append(line)

    for row in data:
        if any(x is None for x in row):
            print(row)

    print("stocks")
    with open("stocks.txt", "r", encoding='utf8', newline='') as f:
        reader = csv.DictReader(f, delimiter="\t")
        data = [parse_dict(row, { 'date' : dateutil.parser.parse,
                                  'closing_price' : float })
                for row in reader]

    max_aapl_price = max(row["closing_price"]
                         for row in data
                         if row["symbol"] == "AAPL")
    print("max aapl price", max_aapl_price)

    # group rows by symbol
    by_symbol = defaultdict(list)

    for row in data:
        by_symbol[row["symbol"]].append(row)

    # use a dict comprehension to find the max for each symbol
    max_price_by_symbol = { symbol : max(row["closing_price"]
                            for row in grouped_rows)
                            for symbol, grouped_rows in by_symbol.items() }
    print("max price by symbol")
    print(max_price_by_symbol)

    # key is symbol, value is list of "change" dicts
    changes_by_symbol = group_by(picker("symbol"), data, day_over_day_changes)
    # collect all "change" dicts into one big list
    all_changes = [change
                   for changes in changes_by_symbol.values()
                   for change in changes]

    print("max change", max(all_changes, key=picker("change")))
    print("min change", min(all_changes, key=picker("change")))

    # to combine percent changes, we add 1 to each, multiply them, and subtract 1
    # for instance, if we combine +10% and -20%, the overall change is
    # (1 + 10%) * (1 - 20%) - 1 = 1.1 * .8 - 1 = -12%
    def combine_pct_changes(pct_change1, pct_change2):
        return (1 + pct_change1) * (1 + pct_change2) - 1

    def overall_change(changes):
        return reduce(combine_pct_changes, pluck("change", changes))

    overall_change_by_month = group_by(lambda row: row['date'].month,
                                       all_changes,
                                       overall_change)
    print("overall change by month")
    print(overall_change_by_month)

    print("rescaling")

    data = [[1, 20, 2],
            [1, 30, 3],
            [1, 40, 4]]

    print("original: ", data)
    print("scale: ", scale(data))
    print("rescaled: ", rescale(data))
    print()

    print("PCA")

    Y = de_mean_matrix(X)
    components = principal_component_analysis(Y, 2)
    print("principal components", components)
    print("first point", Y[0])
    print("first point transformed", transform_vector(Y[0], components))