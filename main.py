from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle


# -----------------------------
# 1. Load Trained Model & Scaler
# -----------------------------
with open("rf_classifier.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

# -----------------------------
# 2. Initialize FastAPI App
# -----------------------------
app = FastAPI(
    title="Diabetes Prediction API",
    description="A simple API that predicts whether a person has diabetes using a trained ML model.",
    version="1.0"
)

# -----------------------------
# 3. Define Input Schema
# -----------------------------
class PatientData(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DPF: float   # DiabetesPedigreeFunction
    Age: int

# -----------------------------
# 4. Prediction Route
# -----------------------------
@app.post("/predict")
def predict(data: PatientData):
    try:
        # Convert input data to array
        input_data = np.array([[data.Pregnancies, data.Glucose, data.BloodPressure,
                                data.SkinThickness, data.Insulin, data.BMI,
                                data.DPF, data.Age]])
        
        # Scale the input
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        result = "Diabetic" if prediction == 1 else "Not Diabetic"
        
        print("CI in Place")
        return {
            "prediction": int(prediction),
            "result": result
        }
    except Exception as e:
        return {"error": str(e)}
