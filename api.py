from fastapi import FastAPI
from Schema.pydantic_model import Ollama_driving
import pickle

with open("Model/ola_driving_churn_model.pkl","rb") as f:
    data = pickle.load(f)

std = data["Standard_scaler"]
lr = data["Logistic_regression"]

