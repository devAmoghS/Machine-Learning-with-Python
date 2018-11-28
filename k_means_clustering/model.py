import random

from k_means_clustering.data import inputs
from k_means_clustering.utils import KMeans, squared_clustering_errors, recolor_image, bottom_up_cluster, \
    generate_clusters, get_values

if __name__ == '__main__':
    random.seed(0)
    cluster = KMeans(3)
    cluster.train(inputs=inputs)
    print("3-means:")
    print(cluster.means)
    print()

    random.seed(0)
    cluster = KMeans(2)
    cluster.train(inputs=inputs)
    print("2-means:")
    print(cluster.means)
    print()

    # for k in range(1, len(inputs) + 1):
    #     print(k, squared_clustering_errors(inputs, k))
    # print()

    # recolor_image('/home/amogh/Pictures/symantec.png')

    print("bottom up hierarchical clustering")

    base_cluster = bottom_up_cluster(inputs)
    print(base_cluster)

    print()
    print("three clusters, min:")
    for cluster in generate_clusters(base_cluster, 3):
        print(get_values(cluster))

    print()
    print("three clusters, max:")
    base_cluster = bottom_up_cluster(inputs, max)
    for cluster in generate_clusters(base_cluster, 3):
        print(get_values(cluster))