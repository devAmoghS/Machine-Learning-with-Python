### Introduction

K-nearest nieghbor is a supervised machine learning algorithm.

### Problem Statement

Given some labelled data points, we have to classify a new data point according to its nearest neigbors.

**Example used here**

We have the data for a large social networking company which ran polls for their favroite programming language. The users belong from a group of large cities. Now the VP of Community Engagement want you to `predict the` **favorite programming language** `for the places that were` **not** `part of the survey`

### Intuition

* In kNN, k is the no. of neigbors you will evaluate to decide which group a new data point will belong to ?
* Value of k is decided by plotting the error rate against the different value of k
* Once the value of k is initiliazed, we take the nearest the k neigbors from the data point
* The measure of distance between the data points can be calculated using either `Euclidean Distance` or `Manhattan Distance`
* Once we calculate the distance of all the k nearest neigbors, we then look for the majority of labels in the neigbots
* The data point is assigned to the group which has maximum no. of neigbors

### Choosing K value
* First divide the entire data set into training set and test set. 
* Apply the KNN algorithm into training set and cross validate it with test set.
* Lets assume you have a train set `xtrain` and test set `xtest`
* Now create the model with `k` value `1` and predict with test set data 
* Check the accuracy and other parameters then repeat the same process after increasing the k value by 1 each time.


Here I am increasing the k value by 1 from `1 to 29` and printing the accuracy with respected `k` value.
![Code](https://qphs.fs.quoracdn.net/main-qimg-9e8fedc07dafba2106eb11f0bfd4ba7d.webp)

### Note

* kNN is impacted by `Imbalanced datasets`. 
Suppose there are `m` instances of **class 1** and `n` insatnces of **class 2** where `n << m`. 
In a case where `k > n`, then this may lead to counting of more instances of m and 
hence it will impact the majority election in k nearest neigbors

* kNN is also very sensitve to `outliers`
