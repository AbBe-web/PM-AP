def calculate_bmi(height_cm, weight_kg):
    """Calculate BMI from height in cm and weight in kg."""
    height_m = height_cm / 100
    bmi = weight_kg / (height_m * height_m)
    return round(bmi, 1)

def validate_age(age):
    """Validate age input."""
    if age < 0 or age > 120:
        return False, "L'âge doit être compris entre 0 et 120 ans"
    return True, ""

def validate_height_weight(height, weight):
    """Validate height and weight inputs."""
    if height <= 0:
        return False, "La taille doit être supérieure à 0"
    if weight <= 0:
        return False, "Le poids doit être supérieur à 0"
    return True, ""

def format_bmi_category(bmi):
    """Return BMI category based on value."""
    if bmi < 18.5:
        return "Insuffisance pondérale"
    elif bmi < 25:
        return "Poids normal"
    elif bmi < 30:
        return "Surpoids"
    else:
        return "Obésité"
