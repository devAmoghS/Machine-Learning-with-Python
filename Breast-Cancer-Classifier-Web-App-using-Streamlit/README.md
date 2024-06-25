# Breast-Cancer-Classifier
This is a Breast Cancer Classifier using Machine Learning.

![Type](https://img.shields.io/badge/Machine-Learning-red.svg)
![IDE](https://img.shields.io/badge/IDE-JupyterNotebook-orange.svg)
![Type](https://img.shields.io/badge/Type-Supervised-yellow.svg)
![Status](https://img.shields.io/badge/Status-Completed-cherryred.svg)

Link to the web app : 

<a href="https://dvamsidhar2002-breast-c-breast-cancer-classifier-web-app-xdlnez.streamlit.app/">
    <img src="https://img.shields.io/badge/Breast Cancer Classifier-0A0A0A?style=plastic&logo=HERE&logoColor=white" height=20></a>



### There are two types of tumours detected in human body : 

<div>
<img align = 'right' src = "Benign tumour.png" alt="Benign tumour" height=230 width=200>
<h2>BENIGN TUMOUR</h2>
<ul>
  <li>  Non - Cancerous
  <li>  Capsulated
  <li>  Non - invasive
  <li>  Slow growing
  <li>  Do not spread to other parts of the body
  <li>  Cells are normal
</ul>
</div>
<br><hr>
<div>
<img align = 'right' src = "Malignant Tumour.png" alt="Malignant tumour" height=230 width=200>
<h2>MALIGNANT TUMOUR</h2>
<ul>
  <li> Cancerous
  <li> Non-Capsulated
  <li> Invasive
  <li> Fast growing
  <li> Spread to other parts of the body
  <li> Cells are abnormal
</ul>
</div>

<h2 align="center">WORKFLOW OF THE PROJECT </h2>

```mermaid
flowchart TD

A[Step 0 : Collect Data] --> B[Step 1 : Import Libraries/Modules in the workspace]
B[Step 1 : Import Libraries/Modules in the workspace] --> C[Step 2 : Import the collected data into the workspace]
C[Step 2 : Import the collected data into the workspace] --> D[Step 3 : Data Preprocessing]
D[Step 3 : Data Preprocessing] --> E[Step 4 : Perform EDA by visualizing the data]
E[Step 4 : Perform EDA by visualizing the data] --> F[Step 5 : Train ML model using LOGISTIC REGRESSION]
F[Step 5 : Train ML model using LOGISTIC REGRESSION] --> G[Step 6 : Deploy ML model as a Web App]
```
