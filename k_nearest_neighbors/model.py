import random
from k_nearest_neighbors.data import cities
from k_nearest_neighbors.utils import knn_classify, random_distances
from helpers.stats import mean

if __name__ == "__main__":

    # try several different values for k
    for k in [1, 3, 5, 7]:
        num_correct = 0

        for location, actual_language in cities:

            other_cities = [other_city
                            for other_city in cities
                            if other_city != (location, actual_language)]

            predicted_language = knn_classify(k, other_cities, location)

            if predicted_language == actual_language:
                num_correct += 1

        print(k, "neighbor[s]:", num_correct, "correct out of", len(cities))

    dimensions = range(1, 101, 5)

    avg_distances = []
    min_distances = []

    random.seed(0)
    for dim in dimensions:
        distances = random_distances(dim, 10000)  # 10,000 random pairs
        avg_distances.append(mean(distances))     # track the average
        min_distances.append(min(distances))      # track the minimum
        print(dim, min(distances), mean(distances), min(distances) / mean(distances))
