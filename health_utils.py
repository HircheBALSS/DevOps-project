def calculate_bmi(height: float, weight: float) -> float:

    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive numbers")
        
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def calculate_bmr(height: float, weight: float, age: int, gender: str) -> float:
    
    if height <= 0 or weight <= 0 or age <= 0:
        raise ValueError("Height, weight, and age must be positive numbers")
        
    gender = gender.lower()
    if gender not in ['male', 'female']:
        raise ValueError("Gender must be 'male' or 'female'")
    
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    return round(bmr, 2)