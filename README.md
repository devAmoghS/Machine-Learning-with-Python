# Machine-Learning-with-Python ![GitHub stars](https://img.shields.io/github/stars/devAmoghS/Machine-Learning-with-Python?style=for-the-badge)  ![GitHub forks](https://img.shields.io/github/forks/devAmoghS/Machine-Learning-with-Python?label=Forks&style=for-the-badge)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=devAmoghS/Machine-Learning-with-Python&type=Date)](https://star-history.com/#devAmoghS/Machine-Learning-with-Python&Date)


![alt text](https://media.istockphoto.com/vectors/machine-learning-3-step-infographic-artificial-intelligence-machine-vector-id962219860?k=6&m=962219860&s=612x612&w=0&h=yricYyUqZbILMHp3IvtenS3xbRDhu1w1u5kk2az5tbo=)

## Small scale machine learning projects to understand the core concepts (order: oldest to newest)
* Topic Modelling using **Latent Dirichlet Allocation** with newsgroups20 dataset, implemented with Python and Scikit-Learn
* Implemented a simple **neural network** built with Keras on MNIST dataset
* Stock Price Forecasting on Google using **Linear Regression**
* Implemented a simple a **social network** to learn basics of Python
* Implemented **Naives Bayes Classifier** to filter spam messages on SpamAssasin Public Corpus
* **Churn Prediction Model** for banking dataset using Keras and Scikit-Learn
* Implemented **Random Forest** from scratch and built a classifier on Sonar dataset from UCI repository
* Simple Linear Regression in Python on sample dataset
* **Multiple Regression** in Python on sample dataset
* **PCA and scaling** sample stock data in Python [working_with_data]
* **Decision Trees** in Python on sample dataset
* **Logistic Regression** in Python on sample dataset
* Built a neural network in Python to defeat a captcha system
* Helper methods include commom operations used in **Statistics, Probability, Linear Algebra and Data Analysis**
* **K-means clustering** with example data; **clustering colors** with k-means; **Bottom-up Hierarchical Clustering**
* Generating Word Clouds
* Sentence generation using n-grams
* Sentence generation using **Grammars and Automata Theory; Gibbs Sampling** 
* Topic Modelling using Latent Dirichlet Analysis (LDA)
* Wrapper for using Scikit-Learn's **GridSearchCV** for a **Keras Neural Network**
* **Recommender system** using **cosine similarity**, recommending new interests to users as well as matching users as per common interests
* Implementing different methods for **network analysis** such as **PageRank, Betweeness Centrality, Closeness Centrality, EigenVector Centrality**
* Implementing methods used for **Hypothesis Inference** such as **P-hacking, A/B Testing, Bayesian Inference**
* Implemented **K-nearest neigbors** for next presedential election and prediciting voting behavior based on nearest neigbors.

## Installation notes
MLwP is built using Python 3.5.  The easiest way to set up a compatible
environment is to use [Conda](https://conda.io/).  This will set up a virtual
environment with the exact version of Python used for development along with all the
dependencies needed to run MLwP.

1.  [Download and install Conda](https://conda.io/docs/download.html).
2.  Create a Conda environment with Python 3. 

(**Note**: enter ```cd ~``` to go on **$HOME** , then perform these commands)

    ```
    conda create --name *your env name* python=3.5
    ```
   
   You will get the following, mlwp-test is the env name used in this example
   
   ```
   Solving environment: done
   
## Package Plan ##

  environment location: /home/user/anaconda3/envs/mlwp-test

  added / updated specs: 
    - python=3.5


The following NEW packages will be INSTALLED:

    ca-certificates: 2018.12.5-0            
    certifi:         2018.8.24-py35_1       
    libedit:         3.1.20181209-hc058e9b_0
    libffi:          3.2.1-hd88cf55_4       
    libgcc-ng:       8.2.0-hdf63c60_1       
    libstdcxx-ng:    8.2.0-hdf63c60_1       
    ncurses:         6.1-he6710b0_1         
    openssl:         1.0.2p-h14c3975_0      
    pip:             10.0.1-py35_0          
    python:          3.5.6-hc3d631a_0       
    readline:        7.0-h7b6447c_5         
    setuptools:      40.2.0-py35_0          
    sqlite:          3.26.0-h7b6447c_0      
    tk:              8.6.8-hbc83047_0       
    wheel:           0.31.1-py35_0          
    xz:              5.2.4-h14c3975_4       
    zlib:            1.2.11-h7b6447c_3      

Proceed ([y]/n)?  *Press y*

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use:
# > source activate mlwp-test
#
# To deactivate an active environment, use:
# > source deactivate
#

   ```
   The environment is successfully created.

3.  Now activate the Conda environment.

    ```
    source activate *your env name*
    ```
    You will get the following
    
    ```
    (mlwp-test) amogh@hp15X34:~$ 
    ```
    Enter `conda list` to get the list of available packages
    
    ```
        (mlwp-test) amogh@hp15X34:~$ conda list
    # packages in environment at /home/amogh/anaconda3/envs/mlwp-test:
    #
    # Name                    Version                   Build  Channel
    ca-certificates           2018.12.5                     0  
    certifi                   2018.8.24                py35_1  
    libedit                   3.1.20181209         hc058e9b_0  
    libffi                    3.2.1                hd88cf55_4  
    libgcc-ng                 8.2.0                hdf63c60_1  
    libstdcxx-ng              8.2.0                hdf63c60_1  
    ncurses                   6.1                  he6710b0_1  
    openssl                   1.0.2p               h14c3975_0  
    pip                       10.0.1                   py35_0  
    python                    3.5.6                hc3d631a_0  
    readline                  7.0                  h7b6447c_5  
    setuptools                40.2.0                   py35_0  
    sqlite                    3.26.0               h7b6447c_0  
    tk                        8.6.8                hbc83047_0  
    wheel                     0.31.1                   py35_0  
    xz                        5.2.4                h14c3975_4  
    zlib                      1.2.11               h7b6447c_3 
    ```

4.  Install the required dependencies.

    ```
    (mlwp-test) amogh@hp15X34:~$ conda install --yes --file *path to requirements.txt*
    ```
    
5. In case you are not able to install the packages or getting `PackagesNotFoundError`
Use the following command ` conda install -c conda-forge *list of packages separated by space*`. For more info, refer issue [#3](https://github.com/devAmoghS/Machine-Learning-with-Python/issues/3) **Unable to install requirements**


## How good is the code ?
* It is well tested
* It passes style checks (PEP8 compliant)
* It can compile in its current state (and there are relatively no issues)

## How much support is available?
* FAQs (coming soon)
* Documentation (coming soon)

## Issues
Feel free to submit issues and enhancement requests.

## Contributing
Please refer to each project's style guidelines and guidelines for submitting patches and additions. In general, we follow the "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!
