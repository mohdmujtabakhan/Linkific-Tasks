# Salary Prediction API using Flask and Machine Learning

## Project Overview

This project demonstrates the complete deployment of a Machine Learning model as a RESTful API using **Flask**. A Linear Regression model is trained on a salary dataset and deployed so that users can send HTTP requests to predict salaries based on years of experience.

The project also demonstrates model serialization, API development, request validation, exception handling, logging, response time calculation, and API testing using Postman.

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | Programming Language |
| Flask | REST API Framework |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Scikit-learn | Machine Learning Model |
| Pickle | Model Serialization |
| Logging Module | Request Logging |
| Time Module | Response Time Measurement |
| Postman | API Testing |
| VS Code | Development Environment |

---

# Project Structure

```
ml-api-deployment/
│
├── app.py
├── Salary_Data.csv
├── salary_model.pkl
├── requirements.txt
├── README.md
├── postman_collection.json

```

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ml-api-deployment.git
```

Go into the project folder

```bash
cd ml-api-deployment
```

Install all dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements

```
Flask
pandas
numpy
scikit-learn
joblib
pickle
```

or install manually

```bash
pip install flask pandas numpy scikit-learn joblib
```

---

# How to Run

Run the Flask application

```bash
python app.py
```

If successful, Flask starts at

```
http://127.0.0.1:5000
```

Open Postman to test all endpoints.

---

# API Endpoints

## 1. Home Endpoint

### URL

```
GET /
```

### Description

Checks whether the API is running.

### Sample Response

```json
Salary Prediction API is Running Successfully!
```

---

## 2. Train Model Endpoint

### URL

```
POST /train
```

### Description

Loads the dataset, trains the Linear Regression model, calculates evaluation metrics, and saves the trained model as **salary_model.pkl**.

### Sample Request

No request body required.

### Sample Response

```json
{
    "message":"Model trained successfully",
    "MSE":31270951.72,
    "R2 Score":0.96
}
```

---

## 3. Predict Salary Endpoint

### URL

```
POST /predict
```

### Sample Request

```json
{
    "experience":5
}
```

### Sample Response

```json
{
    "Experience":5,
    "Predicted Salary":73042.34,
    "Response Time (seconds)":0.0017
}
```

---

## 4. Model Information Endpoint

### URL

```
GET /model-info
```

### Description

Returns information about the trained model including evaluation metrics.

### Sample Response

```json
{
    "Model":"Linear Regression",
    "Dataset":"Salary_Data.csv",
    "Target":"Salary",
    "Feature":"Years of Experience",
    "MSE":31270951.72,
    "R2 Score":0.96
}
```

---

# Sample Requests

## Predict Salary

```json
{
    "experience":3
}
```

---

```json
{
    "experience":7
}
```

---

```json
{
    "experience":12
}
```

---

# Sample Responses

```json
{
    "Experience":3,
    "Predicted Salary":56500.45,
    "Response Time (seconds)":0.0012
}
```

---

```json
{
    "Experience":7,
    "Predicted Salary":92000.87,
    "Response Time (seconds)":0.0014
}
```

---

# Input Validation

The API validates every request before making predictions.

Validation includes:

- Checking JSON request format
- Ensuring the experience field is present
- Verifying numeric input
- Rejecting empty requests
- Returning appropriate HTTP status codes

Example Invalid Request

```json
{}
```

Response

```json
{
    "error":"Please provide experience."
}
```

Status Code

```
400 Bad Request
```
---

# Error Handling

The application uses **try-except blocks** throughout the API.

Handled errors include

- Missing input
- Invalid JSON
- Model loading failures
- Prediction failures
- Unexpected exceptions

Example Response

```json
{
    "error":"Internal Server Error"
}
```

Status Code

```
500 Internal Server Error
```

---

# Logging

The application records important API events using Python's Logging module.

Logged information includes

- Incoming prediction requests
- Prediction completion
- Errors during execution
- Response time

Example Log

```
Prediction request received.
Prediction completed in 0.0014 seconds.
```

---

# Response Time

Each prediction request calculates execution time.

Example

```json
{
    "Response Time (seconds)":0.0013
}
```

This helps evaluate API performance.

---

# Model Serialization

The trained Linear Regression model is stored using Python Pickle.

Saving model

```python
with open("salary_model.pkl","wb") as file:
    pickle.dump(model,file)
```

Loading model

```python
with open("salary_model.pkl","rb") as file:
    model=pickle.load(file)
```

Model serialization allows the trained model to be reused without retraining every time the server starts.

---

# API Testing

All API endpoints were tested successfully using **Postman**.

Tested endpoints include

- GET /
- POST /train
- POST /predict
- GET /model-info

The exported Postman collection is included in the repository.

```
postman_collection.json
```

---

# Future Improvements

Future enhancements for this project include

- Docker containerization
- Cloud deployment (Render, Railway, AWS)
- Authentication using JWT
- Swagger/OpenAPI documentation
- Database integration
- Multiple ML models
- Model versioning
- Batch prediction endpoint
- CI/CD pipeline
- Automated unit testing

---

# Author

**Mohammed Mujtaba Khan**

Artificial Intelligence and Machine Learning Engineer

GitHub:
https://github.com/mohdmujtabakhan

---

# License

This project is developed for educational purposes as part of Machine Learning API Deployment practice.
