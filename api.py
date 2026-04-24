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