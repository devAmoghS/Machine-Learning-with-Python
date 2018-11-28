import random
import matplotlib.image as mpimg
from helpers.linear_algebra import squared_distance, vector_mean, distance
import matplotlib.pyplot as plt


class KMeans:
    """perfroms k-means clustering"""

    def __init__(self, k):
        self.k = k  # number of clusters
        self.means = None  # means of clusters

    def classify(self, input):
        """return the index of cluster closest to the input"""
        return min(range(self.k),
                   key=lambda i: squared_distance(input, self.means[i]))

    def train(self, inputs):
        """choose k random points as the initial means"""
        self.means = random.sample(inputs, self.k)
        assignments = None
        while True:

            # Find new assignments
            new_assignments = list(map(self.classify, inputs))
            # if no assignments have changed, we're done
            if assignments == new_assignments:
                return
            # otherwise keep the new assignments
            assignments = new_assignments

            # and compute the new means based on the new assignments
            for i in range(self.k):
                i_points = [p for p, a in zip(inputs, assignments) if a == i]

                if i_points:
                    self.means[i] = vector_mean(i_points)


def squared_clustering_errors(inputs, k):
    """finds the total squared error from k-means clustering the inputs"""
    clusterer = KMeans(k)
    clusterer.train(inputs=inputs)
    means = clusterer.means
    assignments = list(map(clusterer.classify, inputs))

    return sum(squared_distance(inputs, means[cluster]) for input, cluster in zip(inputs, assignments))


"""Clustering Colors"""


def recolor_image(input_file, k=5):
    img = mpimg.imread(input_file)
    pixels = [pixel for row in img for pixel in row]
    clusterer = KMeans(k)
    clusterer.train(pixels)  # this might take a while

    def recolor(pixel):
        cluster = clusterer.classify(pixel)  # index of the closest cluster
        return clusterer.means[clusterer]  # mean of the closest cluster

    new_img = [[recolor(pixel) for pixel in row] for row in img]
    plt.imshow(new_img)
    plt.axis('off')
    plt.show()


"""Bottom up Hierarchical Clustering"""


def is_leaf(cluster):
    """a cluster is a leaf if it has length 1"""
    return len(cluster) == 1


def get_children(cluster):
    """returns the two children of this cluster if it's a merged cluster;
    raises an Exception if this is a leaf cluster"""
    if is_leaf(cluster):
        raise TypeError("a leaf cluster has no children")
    else:
        return cluster[1]


def get_values(cluster):
    """returns the value in this cluster (if it's a leaf cluster)
    or all the values in the leaf clusters below it (if it's not)"""
    if is_leaf(cluster):
        return cluster  # is already a 1-tuple containing value
    else:
        return [value
                for child in get_children(cluster)
                for value in get_values(child)]


def cluster_distance(cluster1, cluster2, distance_agg=min):
    """finds the aggregate distance between elements of
    cluster1 and elements of cluster2"""
    return distance_agg([distance(input1, input2)
                         for input1 in get_values(cluster1)
                         for input2 in get_values(cluster2)])


def get_merge_order(cluster):
    if is_leaf(cluster):
        return float('inf')
    else:
        return cluster[0]


def bottom_up_cluster(inputs, distance_agg=min):
    # start with every input leaf cluster
    clusters = [(input) for input in inputs]

    # as long as we have more than one cluster left...
    while len(clusters) > 1:
        # find the two closest clusters
        c1, c2 = min([(cluster1, cluster2)
                      for i, cluster1 in enumerate(clusters)
                      for cluster2 in clusters[:i]],
                     key=lambda p: cluster_distance(p[0], p[1], distance_agg))

        # remove them from the list of clusters
        clusters = [c for c in clusters if c != c1 and c != c2]

        # merge them, using merge _order = # of cluster left
        merged_cluster = (len(clusters), [c1, c2])

        # add their merge
        clusters.append(merged_cluster)

    # when there is only one cluster left, return it
    return clusters[0]


def generate_clusters(base_cluster, num_clusters):
    # start with a list of just a base cluster
    clusters = [base_cluster]

    # as long as we don't have enough clusters
    while len(clusters) < num_clusters:
        # choose the last-merged of our clusters
        next_cluster = min(clusters, key=get_merge_order)
        # remove it from the list
        clusters = [c for c in clusters if c != next_cluster]
        # and add its children to the list (i.e. unmerge it)
        clusters.extend(get_children(next_cluster))

    return clusters
