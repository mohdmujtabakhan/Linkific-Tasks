from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import pickle

import logging
import time

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

app = Flask(__name__)
logging.basicConfig(
    filename="api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route("/")
def home():
    return "Salary Prediction API is Running Successfully!"


@app.route("/train", methods=["POST"])
def train():

    try:
        logging.info("Training endpoint called.")

        data = pd.read_csv("Salary_Data.csv")

        data.columns = data.columns.str.strip()

        data = data.dropna()

        X = data[["Years of Experience"]]

        y = data["Salary"]

        model = LinearRegression()

        model.fit(X, y)

        predictions = model.predict(X)

        mse = mean_squared_error(y, predictions)

        r2 = r2_score(y, predictions)

        with open("salary_model.pkl", "wb") as file:
            pickle.dump(model, file)

        return jsonify({
            "message": "Model trained successfully",
            "MSE": round(mse,2),
            "R2 Score": round(r2,2)
        })

    except Exception as e:
        logging.error(str(e))
        return jsonify({"error": str(e)}),500
    

@app.route("/predict", methods=["POST"])
def predict():
    try:
        start_time = time.time()
        logging.info("Prediction request received.")

        data = request.get_json()

        if "experience" not in data:
            return jsonify({"error": "Please provide experience."}), 400

        experience = float(data["experience"])

        with open("salary_model.pkl", "rb") as file:
            model = pickle.load(file)

        input_data = pd.DataFrame({
            "Years of Experience": [experience]
        })

        prediction = model.predict(input_data)

        end_time = time.time()
        response_time = round(end_time - start_time, 4)

        logging.info(f"Prediction completed in {response_time} seconds")

        return jsonify({
            "Experience": experience,
            "Predicted Salary": round(float(prediction[0]), 2),
            "Response Time (seconds)": response_time
        })

    except Exception as e:
        logging.error(str(e))
        return jsonify({"error": str(e)}), 500
        
@app.route("/model-info", methods=["GET"])
def model_info():

    try:

        data = pd.read_csv("Salary_Data.csv")

        data.columns = data.columns.str.strip()

        data = data.dropna()

        X = data[["Years of Experience"]]

        y = data["Salary"]

        with open("salary_model.pkl","rb") as file:

            model = pickle.load(file)

        predictions = model.predict(X)

        mse = mean_squared_error(y,predictions)

        r2 = r2_score(y,predictions)

        return jsonify({

            "Model":"Linear Regression",

            "Feature":"Years of Experience",

            "Target":"Salary",

            "Mean Squared Error":round(mse,2),

            "R2 Score":round(r2,2),

            "Status":"Model Loaded Successfully"

        })

    except Exception as e:

        return jsonify({"error":str(e)}),500

if __name__ == "__main__":
    app.run(debug=True)