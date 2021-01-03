### 1. What is multi-collinearity

When two or more predictors are highly correlated to each other such that one predictor 
can be derived using the linear combinations of other predictors, then the predictors are said to be collinear

### 2. What is the difference between standardisation and normalization ? Why is it useful?
Standardisation is a scclaing technique in which values are shifted and rescaled so that the mean is 0 and the variance is 1

Normalization is a scaling technique in which values are shifted and rescaled so that they end up ranging between 0 and 1. It is also known as Min-Max scaling

* Algorithms which use gradient descent based optimisation (linear regression, logistic regression, neural networks) will require features to be scaled so that optimization will be faster and the convergence will be more accurate.
* **Having features on a similar scale can help the gradient descent converge more quickly towards the minima.**
* Distance algorithms like KNN, K-means, and SVM are most affected by the range of features. This is because behind the scenes they are using distances between data points to determine their similarity.
* **Therefore, we scale our data before employing a distance based algorithm so that all the features contribute equally to the result.**

![](https://i.pinimg.com/originals/1c/16/04/1c160466f8bfd26ca66a44f79514fb5d.jpg)

### 3. What is the central limit theorem ? Why is it useful ?
The Central Limit Theorem is about how the sum of many different independent random variables tends towards a normal distribution (bell curve).

For example: suppose you're rolling 2 6-sided dice. The rolls are all independent because one of the rolls doesn't affect any of the other rolls. For a single die, the distribution is the same chance for 1 2 3 4 5 and 6.

But of you add the sum of 2 dice, you will notice that you have a 1/36 chance to get a 2, 2/36 chance to get a 3, 3/36 chance to get a 4, ..., up until 6/36 chance of getting a 7, then the chance decreases again until you're back at 1/36 chance of getting a 12. This is because the values in the middle, like 7, can be reached by getting 1+6, 6+1, 2+5, 5+2, 3+4 and 4+3, whereas the edges like 2 require a single very specific result (1+1) where every single die needs to land on 1.

If you further increase the number of dice you roll, the edge cases become less and less likely, because they keep requiring very specific results, whereas the results in the middle become more likely. The more dice you add, the more it will eventually look like a bell curve.

![](https://prwatech.in/blog/wp-content/uploads/2019/06/CetralLimitThm-1024x512.png)

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
### 24. Does a low coefficient of determination always mean that my model is bad or vice versa ? Explain.
* R-squared does not measure goodness of fit.
* R-squared does not measure predictive error.
* R-squared does not allow you to compare models using transformed responses.
* R-squared does not measure how one variable explains another.

Ref:- https://data.library.virginia.edu/is-r-squared-useless/#:~:text=Let's%20recap%3A-,R%2Dsquared%20does%20not%20measure%20goodness%20of%20fit.,how%20one%20variable%20explains%20another.

### 24. What is the difference between probability and likelihood ?
### 25. What is the difference between generative and discriminative models ?
### 26. How is a decision tree pruned ?
### 27. What do you understand by the bias variance tradeoff ? 

![](https://djsaunde.files.wordpress.com/2017/07/bias-variance-tradeoff.png)

Bias ia how well the model fits the data. Variance tells us the magnitude of change in the model based on the change in data
a. Very simple models have high bias and low variance eg. linear models 
b. Very complex models have low bias and high variance eg. tree based models. Hence they are more prone to overfitting.

How to deal with them ?

| High Bias                                    | High Variance |   |
|----------------------------------------------|---------------|---|
| Try getting additional features              | Try getting more training examples              |   |
| Try adding polynomial features               | Try smaller set of features              |   |
| Try to decrease the regularization parameter | Try to increase the regularization parameter              |   |
