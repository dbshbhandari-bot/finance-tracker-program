from first import predict_patient_flow
result = predict_patient_flow(
    day=10,
    infection_rate=0.05,
    beds_available=120
)

print("Predicted patients:", result)
if predict_patient_flow > beds_available:
    suggestion = "Increase bed capacity or delay elective admissions."

