def generate_suggestions(predicted_patients, beds_available):
    suggestions = []

    if predicted_patients > beds_available:
        suggestions.append("⚠️ Risk of bed shortage")
        suggestions.append("Consider postponing non-urgent procedures")
        suggestions.append("Activate overflow or surge capacity")

    if predicted_patients > beds_available * 1.2:
        suggestions.append("🚨 Emergency staffing required")
        suggestions.append("Call in temporary staff")

    if predicted_patients < beds_available * 0.7:
        suggestions.append("Beds underutilized")
        suggestions.append("Good day for elective admissions")

    return suggestions
