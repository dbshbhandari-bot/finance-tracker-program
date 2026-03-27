def resource_plan(predicted_patients):
    return {
        "masks_required": predicted_patients * 2,
        "gloves_required": predicted_patients * 4,
        "sanitizer_units": predicted_patients // 10
    }
