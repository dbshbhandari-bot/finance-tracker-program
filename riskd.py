def calculate_risk(patient_forecast, infection_forecast, beds_available):
    score = 0
    reasons = []

    if patient_forecast > beds_available:
        score += 2
        reasons.append("Patient demand exceeds bed capacity")

    if infection_forecast > 0.1:
        score += 2
        reasons.append("Infection rate is trending upwards")

    if patient_forecast > beds_available * 1.2:
        score += 3
        reasons.append("Severe patient surge expected")

    if score >= 5:
        level = "HIGH"
    elif score >= 3:
        level = "MEDIUM"
    else:
        level = "LOW"

    return level, reasons
