from ai  import  generate_suggestions

suggestions = generate_suggestions(
    predicted_patients=180,
    beds_available=120
)

for s in suggestions:
    #print(s)
 from dib  import calculate_staff_needed
 staff = calculate_staff_needed(180)
 print(staff)
