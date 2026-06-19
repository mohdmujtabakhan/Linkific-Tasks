# Salary Prediction System using Linear Regression

## Project Overview

This project implements a Machine Learning-based Salary Prediction System using the Linear Regression algorithm. The model predicts an employee's salary based on their years of professional experience.

The project demonstrates the complete Machine Learning workflow, including data preprocessing, handling missing values, model training, prediction, performance evaluation, and model persistence using Pickle.

---

## Machine Learning Type

**Supervised Learning**

In supervised learning, the model learns from labeled data where both input features and target values are available.

For this project:

* **Feature (Input):** Years of Experience
* **Target Variable (Output):** Salary

---

## Dataset Information

Dataset: `Salary_Data.csv`

The dataset contains employee-related information including:

* Age
* Gender
* Education Level
* Job Title
* Years of Experience
* Salary

For this project, only **Years of Experience** was used as the feature to predict **Salary**.

---

## Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the dataset using Pandas.
2. Inspected dataset structure and data types.
3. Checked for missing values.
4. Removed rows containing missing values.
5. Selected relevant feature and target columns.
6. Prepared data for model training.

---

## Train-Test Split

The dataset was divided into:

* **Training Data:** 80%
* **Testing Data:** 20%

The training dataset was used to train the model, while the testing dataset was used to evaluate its performance on unseen data.

---

## Model Used

**Linear Regression**

Linear Regression is a supervised learning algorithm used to predict continuous numerical values by learning the relationship between input features and target variables.

---

## Model Performance

The trained model was evaluated using the following performance metrics:

| Metric                         | Value          |
| ------------------------------ | -------------- |
| Mean Squared Error (MSE)       | 982,050,061.92 |
| Root Mean Squared Error (RMSE) | 31,337.68      |
| R² Score                       | 0.656          |

### Performance Interpretation

* **MSE** measures the average squared prediction error.
* **RMSE** represents the average prediction error in salary units.
* **R² Score** indicates how much variation in salary is explained by the model.

The model achieved an **R² Score of 0.656**, meaning it explains approximately **65.6% of the variation in employee salaries** based on years of experience.

Since salary is influenced by additional factors such as education level, job title, skills, and age, the model's performance can be further improved by incorporating more features.

---

## Project Files

```text
Salary-Prediction-System/
│
├── Salary_Data.csv
├── ml-basics.ipynb
├── salary_model.pkl
├── README.md

```

---

## Saved Model

The trained model has been saved using **Pickle**.

File:

```text
salary_model.pkl
```

This allows the model to be reused without retraining.

---

## How to Load and Use the Saved Model

### Step 1: Import Pickle

```python
import pickle
```

### Step 2: Load the Saved Model

```python
with open("salary_model.pkl", "rb") as file:
    model = pickle.load(file)

print("Model loaded successfully!")
```

### Step 3: Make Predictions

Predict salary for an employee with 7 years of experience:

```python
salary = model.predict([[7]])

print("Predicted Salary:", salary[0])
```

---

## Requirements

Install the required libraries:

```bash
pip install pandas numpy scikit-learn
```

---

## Conclusion

This project successfully demonstrates the complete Machine Learning pipeline using Linear Regression for salary prediction.

Key achievements:

* Loaded and explored a real-world dataset
* Cleaned and preprocessed data
* Handled missing values
* Performed an 80-20 train-test split
* Trained a Linear Regression model
* Evaluated model performance using MSE, RMSE, and R² Score
* Saved the trained model using Pickle
* Enabled future predictions using the saved model

This project serves as a foundational example of supervised learning and predictive modeling using Python and Scikit-Learn.
