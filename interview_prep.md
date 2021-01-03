### 1. What is multi-collinearity

When two or more predictors are highly correlated to each other such that one predictor 
can be derived using the linear combinations of other predictors, then the predictors are said to be collinear

### 2. What is the difference between standardisation and normalization ? Why is it useful?
### 3. What is the central limit theorem ? Why is it useful ?
### 4. What is the inter quartile range ? Why is it useful ?
### 5. What is the difference between t-test and z-test ? Why is it useful ?
### 6. Why do we take n-1 when calculating sample variance? Why is it useful ?
Read about Besel correction
### 7. What are the assumptions of the normal distribution ? Why is it useful ?
### 8. What are the different approches to outlier detection ?  How will you handle the outliers? Why is it useful ?
### 9. Where is RMSE a bad case ? How do we solve this ?
### 10. What are the loss functions used in logistic regression ?
log loss function
### 11. Explain random forest in laymen terms ?
### 12. How does logisitc regression work in laymen terms ?
### 13. Why is logistic regression bad idea for multiclass classification ?
### 14. How do you perform the train test split in a timeseries modelling ?
### 15. What is the impact on timeseries model in case we have latge variation in data ?
### 16. How do you decide the value of K(value of clusters) in K-means clustering ?
### 17. What are the advantages and disadvantages of undersampling and oversampling ?
### 18. Which are some supervised algorithms that are not impacted by imbalanced data ?
### 19. You are a placement coordinator, you have to design a system for resume recommendation aligning to a company's requirement ?
a. K means clustering to make clusters
b. Ranking algorithm to sort for relevance

_Second Strategy_

a. Perform document similarity using Hamming distance (distance based approach)
b. Compute the JD document distance with the resumes
c. Shortlist top K resumes 

### 20. How will you encode a feature like PinCode which has very high number of discrete values?
Target mean encoding
### 21. How do you design the architecture of a neural network?

## Section II

| Algorithm               | Problem Identification | Evaluation Metric                                                                               | Bias Variance | Impact of outliers | Impact of imbalanced data |   |
|-------------------------|------------------------|-------------------------------------------------------------------------------------------------|---------------|--------------------|---------------------------|---|
| Linear Regression       | Regression             | - Coefficient of determination (R2) - Adjusted R2 - Root Mean Square Error (RMSE) - Mean Absolute Error (MAE) - Root Mean Squared Logarithmic Error (RMSLE)| - High Bias Low Variance               | -Impacted by outliers                   |                           |   |
| Logistic Regression     | Classification         | - Accuracy - Precision - Recall - F-beta score - Area under ROC curve                           | - High Bias Low Variance               | -Impacted by outliers                    |                           |   |
| Support Vector Machines | Classification         | - Accuracy - Precision - Recall - F-beta score - Area under ROC curve                                                                                                | - Low Bias High Variance               | Sensitive to outliers                    | Sensitive to imbalanced data                          |   |
| K-nearest neighbors     | Classification         | - Accuracy - Precision - Recall - F-beta score - Area under ROC curve                                                                                                | - Low Bias High Variance                | Sensitive to outliers                   | Sensitive to imbalanced data                           |   |
| Decision Tree           | Both                   | Both                                                                                                | - Low Bias High Variance                 | - Not impacted by outliers                   | - Not impacted by imbalanced data                           |   |
| Random Forest           | Both                   | Both                                                                                                | - Low Bias High Variance                 | - Not impacted by outliers                   | - Not impacted by imbalanced data                          |   |
| K-means clustering      | Clustering             | - Elbow method - Silhoutte Analysis                                                                                                 |               | Senstive to Outliers                   |                           |   |
|                         |                        |                                                                                                 |               |                    |                           |   |

### 22. Why do CNNs perfom better with images ? (What is it that CNN achieve better than ANN when delaing with image data)
### 23. Explain K-means clustering in laymen terms ?
### 24. What is the evaluation metric for K-means clustering ?
### 25. What is the impact of outliers on K-means clustering ?
### 26. What is the impact of outliers on K-nearest neigbors ?
### 25. What is the impact of imbalanced data on K-means clustering ?
### 26. What is the impact of imbalanced data on K-nearest neigbors ?
