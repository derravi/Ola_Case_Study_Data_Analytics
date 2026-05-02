from fastapi import FastAPI,HTTPException
from Schema.pydantic_model import Ollama_driving
import pickle
import pandas as pd
import numpy as np

data = None

try:
    with open("Model/ola_driving_churn_model.pkl","rb") as f:
        data = pickle.load(f)

except Exception as e:
    raise RuntimeError(f"Model loading failed: {e}")

except Exception as e2:
    print(f"Error : {e2}")

 
if data is None:
    raise RuntimeError("Model not loaded properly")

std = data["Standard_scaler"]
lr = data["Logistic_regression"]

try:
    app = FastAPI(title="Olla Driver Churn prediction")
except Exception as ap:
    print(f"Error:{ap}")
    
@app.get("/")
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

    try:
        df_std = std.transform(df)
        prediction_output = lr.predict(df_std)[0]
    except Exception as e3:
        raise HTTPException(status_code=500,detail=str(e3))
    
    if prediction_output == 0:
        return {"message":"The driver is not likely to churn."}
    else:
        return {"message":"The driver is likely to churn."}