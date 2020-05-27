### Introduction

* K-means clustering is an unsupervised machine learning algorithm.
* K-means algorithm is an iterative algorithm that tries to partition the dataset into `K` pre-defined distinct non-overlapping subgroups(clusters) where each data point belongs to only one group. 
* It tries to make the intra-cluster data points as similar as possible while also keeping the clusters as different (far) as possible. 
* It assigns data points to a cluster such that the sum of the squared distance between the data points and the cluster’s centroid (arithmetic mean of all the data points that belong to that cluster) is at the minimum. 
* The less variation we have within clusters, the more homogeneous (similar) the data points are within the same cluster

### Problem Statement

Given some **unlabelled** data points, we have to identify subgroups such that 
1. Points in the same subgroup are similar to each other.
2. Points in different subgroup are dissimilar to each other.

**Example used here**

We have the data for a large social networking company which is planning to host meetups for their users. We have the users' location data. Now the VP of Growth want you to `choose the` **meetup locations** `so it becomes convinient for everyone to attend`

### Intuition

* In K-means, `k` is the `no. of subgroups` you want the data to be segregated into ?
* Optimal value of `k` can be derived by using `elbow method` (discussed below)
**Centroid Initialization**
* We begin by initializing `k` random data points as the centroids (first pass)
* The measure of distance between the data points and centroids can be calculated using either `Euclidean Distance` or `Manhattan Distance`

**Iteration**
* **Cluster assigment:** We assign a cluster to the data point that is nearest to it.
* Once all the points are assigned to their nearest centroids, then for each cluster the centroid is calculated again using centroid initialization step.
* With the new centroids, we repeat the step of cluster assignment.
* These two steps are iterated as long as `there is no change in cluster assigment of data points` i.e. no data point is moving into a new cluster.

### Choosing K value - Elbow method
* Elbow method gives us an idea on what a good k number of clusters.
* This is based on the sum of squared distance (SSE) between data points and their assigned clusters’ centroids. 
* We pick `k` at the spot where SSE starts to flatten out and forming an elbow. 

Here I am increasing the k value by 1 from `1 to 10` and printing the sum of squared distance with respected `k` value.
![Code](https://miro.medium.com/max/866/1*9z8erk4kvsnxkfv-QhsHZg.png)

### Note

* K-means gives more weight to the bigger clusters.
* K-means assumes spherical shapes of clusters (with radius equal to the distance between the centroid and the furthest data point) and doesn’t work well when clusters are in different shapes such as elliptical clusters.
* If there is overlapping between clusters, K-means doesn’t have an intrinsic measure for uncertainty for the examples belong to the overlapping region in order to determine for which cluster to assign each data point.
* K-means may still cluster the data even if it can’t be clustered such as data that comes from uniform distributions.
