# Classification Models Comparison using Iris Dataset

## Project Overview

This project compares four popular supervised machine learning classification algorithms using the Iris dataset. The objective is to predict the species of an Iris flower based on its physical measurements and identify the best-performing classification model.

The models compared in this project are:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. K-Nearest Neighbors (KNN)

---

## Dataset Information

The Iris dataset is a well-known classification dataset containing 150 flower samples belonging to three species:

* Iris Setosa
* Iris Versicolor
* Iris Virginica

### Features Used

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

### Target Variable

* Flower Species

---

## Machine Learning Type

**Supervised Learning**

In supervised learning, the model learns from labeled data where both the input features and the correct output labels are available during training.

---

## Data Preparation

The following preprocessing steps were performed:

* Loaded the Iris dataset from Scikit-Learn
* Converted the dataset into a Pandas DataFrame
* Explored dataset structure and statistics
* Split the dataset into training and testing sets

### Train-Test Split

* Training Data: 80%
* Testing Data: 20%

---

## Models Implemented

### 1. Logistic Regression

A classification algorithm that predicts class probabilities and assigns the class with the highest probability.

### 2. Decision Tree

A tree-based model that classifies data by creating decision rules based on feature values.

### 3. Random Forest

An ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

### 4. K-Nearest Neighbors (KNN)

A distance-based algorithm that classifies a new sample based on the majority class of its nearest neighbors.

---

## Evaluation Metrics

The following metrics were used to evaluate model performance:

### Accuracy

Measures the percentage of correct predictions made by the model.

### Precision

Measures how many predicted classes were actually correct.

### Recall

Measures how many actual classes were correctly identified.

### F1 Score

Provides a balanced measure of Precision and Recall.

### Confusion Matrix

Visualizes correct and incorrect classifications for each class.

### Cross Validation

Provides a more reliable estimate of model performance by evaluating the model multiple times on different subsets of data.

---

## Model Performance Comparison

| Model               | Accuracy | Precision | Recall | F1 Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | 1.00     | 1.00      | 1.00   | 1.00     |
| Decision Tree       | 0.97     | 0.97      | 0.97   | 0.97     |
| Random Forest       | 1.00     | 1.00      | 1.00   | 1.00     |
| KNN                 | 1.00     | 1.00      | 1.00   | 1.00     |

---

## Best Performing Model

### Random Forest Classifier

Random Forest was selected as the best-performing model because:

* It achieved the highest accuracy score.
* It achieved excellent Precision, Recall, and F1 Score.
* It combines multiple decision trees, making it more robust than a single Decision Tree.
* It reduces overfitting while maintaining high prediction accuracy.
* It generally performs well on unseen data and is considered one of the most reliable classification algorithms.

Although Logistic Regression and KNN achieved similar accuracy scores on the Iris dataset, Random Forest was chosen because of its ability to generalize better and handle more complex datasets.

---

## Why Did Multiple Models Achieve 100% Accuracy?

The Iris dataset is a clean and well-structured dataset with clearly separable classes. Because of this, several classification algorithms can correctly classify all testing samples and achieve 100% accuracy.

To ensure the results were reliable, cross-validation was also performed in addition to the train-test evaluation.

---

## Key Learnings

Through this project, the following concepts were learned and implemented:

* Classification using supervised learning
* Logistic Regression
* Decision Tree Classification
* Random Forest Classification
* K-Nearest Neighbors (KNN)
* Accuracy, Precision, Recall, and F1 Score
* Confusion Matrix Visualization
* Cross Validation
* Model Comparison and Selection

---

## Conclusion

This project successfully compared four supervised classification algorithms using the Iris dataset. All models performed exceptionally well due to the simplicity and separability of the dataset. Random Forest was identified as the best overall model because it achieved excellent performance while providing better robustness and generalization compared to the other algorithms.

The project demonstrates the complete machine learning classification workflow, from data loading and preprocessing to model evaluation and comparison.
