import pandas as pd
import numpy as np

days = 180
data = {
    "day": range(days),
    "patients_arrived": np.random.poisson(120, days),
    "infection_rate": np.random.uniform(0.02, 0.15, days),
    "beds_available": np.random.randint(50, 200, days)
}

df = pd.DataFrame(data)

# ✅ SAVE TO CSV
df.to_csv("hospital_data.csv", index=False)

print("CSV file created successfully!")
print(df)
import joblib

# Load trained model
model = joblib.load("models/patient_flow_model.pkl")

def predict_patient_flow(day, infection_rate, beds_available):
    input_data = pd.DataFrame([{
        "day": day,
        "infection_rate": infection_rate,
        "beds_available": beds_available
    }])

    prediction = model.predict(input_data)
    return int(prediction[0])

