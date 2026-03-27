def generate_recommendations(risk_level):
    if risk_level == "HIGH":
        return [
            "Increase temporary bed capacity",
            "Activate infection prevention escalation",
            "Adjust staff scheduling proactively"
        ]
    elif risk_level == "MEDIUM":
        return
