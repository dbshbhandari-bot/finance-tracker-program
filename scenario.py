def simulate_scenario(
    patient_forecast,
    infection_forecast,
    beds_available,
    bed_change_pct,
    patient_change_pct
):
    adjusted_beds = beds_available * (1 + bed_change_pct / 100)
    adjusted_patients = patient_forecast * (1 + patient_change_pct / 100)

    return adjusted_patients, adjusted_beds
