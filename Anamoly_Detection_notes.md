Inspired from the following [blog post](https://iwringer.wordpress.com/2015/11/17/anomaly-detection-concepts-and-techniques/): 
Kudos to [Srinath Perera](https://www.linkedin.com/in/srinathperera) for writing this 👍

## Anomaly Detection

![Image](https://iwringer.files.wordpress.com/2015/11/anomelydetectionmethods.jpg?w=656)

Four common classes of machine learning applications:

a. classification <br>
b. predicting next value [also known as regression] <br>
c. anamoly detection <br>
d. discovering data strucuture <br>

### Anamoly Detection
As the name suggests, the core focus of anamoly detection is to identify data points that deos not align with the rest of the data. In statistics, these data points are also referred as `outliers`

#### Outliers
Having outliers have **significant effect on the mean and the standard deviation** of your data and hence your results are skewed if they are not dealt properly

#### Applications of Anamoly Detection
Here are some of the examples where anamoly detection is heavily employed:
a. fraud detection <br>
b. surveillance <br>
c. diagnosis <br>
d. data cleanup <br>
e. monitring predicitive maintenance [IoT devices]

##### Since data is categorised as anomalous and non-anomalous, can't we solve it using classification ?
This assumption is correct as long as the following three conditions hold good:

a. Training data present with us is labelled <br>
b. Anomalous and non-anomalous classes are balanced (at least 1:5 proportion) <br>
c. Present data point is not dependent on paast data points [not suitable for time series]

#### Reality
a. Hard to obtain labelled training data all the time <br>
b. Real-life scenarios have heavily imbalanced classes, for e.g. fraud detection in credit cards can have the distribution of 1:10^x where x can go from 3 to 6 <br>
c. One more caveat is that of precision and recall scores for such classifiers ? What is the cost of missing a false positive or a false negative ? <br>
[**Precision** governs of how many anomalies detected by classifiers are truly anamolies] <br>
[**Recall** governs of how many anomalies the classifier is able to capture]

### Types of Anomalies
a. **Point Anomalies**: Individual instance of data is considered as anomalous with respect to rest of data (e.g. purchase with a large transaction value) <br>
b. **Contexual Anomalies**: The instance of data is considered as anomalous with respect to the context, but not otherwise (e.g. large spike in a trend at middle of night) <br>
c. **Collective Anomalies**: Unlike the previous two, here we consider a collection of data instances making up for an anomaly with respect to the rest of data <br>
  i. Events that are actually ordered but showing a degree of disorder (e.g. rhythm in ECG) <br>
  ii. Unexpected value comnbinations (e.g. buying a large number of expensive items) <br>
