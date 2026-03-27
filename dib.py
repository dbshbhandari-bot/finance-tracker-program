def calculate_staff_needed(predicted_patients):
    # Rough rule: 1 nurse per 5 patients
    nurses = predicted_patients // 5

    # 1 doctor per 20 patients
    doctors = predicted_patients // 20

    return {
        "nurses_needed": nurses,
        "doctors_needed": doctors
    }
