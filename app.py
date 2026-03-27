import streamlit
import streamlit as st
from first  import predict_patient_flow
from ai import generate_suggestions
from dib import calculate_staff_needed
from res  import resource_plan
from inf import infection_risk_alert
from inf import estimate_infection_rate
from x import forecast_series
from recom import  generate_recommendations
from scenario import simulate_scenario
from riskd import calculate_risk
st.title("AI Hospital Operations Dashboard")
day = st.number_input("Day", 1, 365, 200)
infection_rate  = estimate_infection_rate(day)
st.info(
    f"Infection risk was automatically estimated based on historical trends: "
    f"{infection_rate:.2%}"
)

beds = st.number_input("Beds Available", 50, 300, 120)

if st.button("Run AI Prediction"):
    predicted = predict_patient_flow(day, infection_rate, beds)

    st.subheader("Predicted Patient Flow")
    st.metric("Expected Patients", predicted)

    st.subheader("AI Suggestions")
    for s in generate_suggestions(predicted, beds):
        st.write("-", s)

    st.subheader("Staff Required")
    st.json(calculate_staff_needed(predicted))

    st.subheader("Resources Needed")
    st.json(resource_plan(predicted))

    st.subheader("Infection Control")
    st.write(infection_risk_alert(infection_rate))
    st.write(infection_risk_alert(infection_rate))














