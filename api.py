from fastapi import FastAPI
from Schema.pydantic_model import Ollama_driving
import pickle
import pandas as pd
import numpy as np

try:
    with open("Model/ola_driving_churn_model.pkl","rb") as f:
        data = pickle.load(f)

except FileNotFoundError as e:
    print(f"Error : {f}")
except Exception as e2:
    print(f"Error : {e2}")

std = data["Standard_scaler"]
lr = data["Logistic_regression"]

app = FastAPI(title="Olla Driver Churn prediction")

@app.get("")
def default_rt():
    return {"message":"Olla Driving Churn Prediciton ML Model"}

@app.post("/prediction")
def predict(data : Ollama_driving):

    df = pd.DataFrame([{
        "Age" : data.age,
        "Gender" : data.gender,
        "Day" : data.day,
        "Month": data.month,
        "Year" : data.year,
        "Education_Level" : data.education_level,
        "Income" : data.income,
        "Joining Designation" : data.joining_designation,
        "Grade" : data.grade,
        "Total Business Value" : data.total_business_value,
        "Quarterly Rating" : data.quarterly_rating
    }])

    df_std = std.transform(df)

    prediction_output = lr.predict(df_std)[0]

    if prediction_output == 0:
        return {"message":"The driver is not likely to churn."}
    else:
        return {"message":"The driver is likely to churn."}