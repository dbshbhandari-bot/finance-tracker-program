import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os
import first
# Load data
df = pd.read_csv("hospital_data.csv")

# Features and target
X = df[["day", "infection_rate", "beds_available"]]
y = df["patients_arrived"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/patient_flow_model.pkl")

print("✅ Patient flow model trained and saved!")


