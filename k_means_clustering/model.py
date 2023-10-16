import random
from k_means_clustering.data import inputs
from k_means_clustering.utils import KMeans, bottom_up_cluster, generate_clusters, get_values

if __name__ == '__main__':
    # Set the random seed for reproducibility
    random.seed(0)

    # Perform k-means clustering with k=3
    kmeans_3 = KMeans(3)
    kmeans_3.train(inputs=inputs)
    print("3-means:")
    print(kmeans_3.means)
    print()

    # Perform k-means clustering with k=2
    kmeans_2 = KMeans(2)
    kmeans_2.train(inputs=inputs)
    print("2-means:")
    print(kmeans_2.means)
    print()

    # Perform hierarchical clustering
    print("Bottom-up hierarchical clustering")
    base_cluster = bottom_up_cluster(inputs)
    print(base_cluster)

    # Generate three clusters with the minimum size
    print("Three clusters, min:")
    for cluster in generate_clusters(base_cluster, 3):
        print(get_values(cluster))

    # Generate three clusters with the maximum size
    print("Three clusters, max:")
    base_cluster = bottom_up_cluster(inputs, max)
    for cluster in generate_clusters(base_cluster, 3):
        print(get_values(cluster))
