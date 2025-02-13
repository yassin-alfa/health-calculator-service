def calculate_bmi(height, weight):
    """Calculate BMI given height in meters and weight in kg."""
    return round(weight / (height ** 2), 2)

def calculate_bmr(height, weight, age, gender):
    """Calculate BMR using the Harris-Benedict equation."""
    if gender.lower() == 'male':
        return round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age), 2)
    elif gender.lower() == 'female':
        return round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age), 2)
    else:
        return None
