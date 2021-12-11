# Import datetime so that it can be
# used to compute a person's age.

from datetime import datetime
# gender = "F"

def main():
    gender = input("Please enter your gender (M or F):").upper()
    birthdate = input("please enter your birthdate (YYYY-MM-DD):")
    pounds = float(input("Enter your weight in US pounds:"))
    inches = float(input("Enter your height in US inches:"))

    # Get the user's gender, birthdate, height, and weight.

    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index,
    # and basal_metabolic_rate functions as needed.
    age = compute_age(birthdate)
    kg = kg_from_lb(pounds)
    cm = cm_from_in(inches)
    bmi = body_mass_index(kg, cm)
    bmr = basal_metabolic_rate(gender, kg, cm, age)

    # Print the results for the user to see.

    print(f"Age (years): {age}")
    print(f"Weight (kg): {kg:.2f}")
    print(f"Height (cm): {cm:.1f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal / day): {bmr:.0f}")
    pass


def compute_age(birth):
    """Compute and return a person's age in years.
    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years


def kg_from_lb(lb):
    """Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    """
    kg = lb * 0.45359237

    return kg


def cm_from_in(inch):
    """Convert a length in inches to centimeters.
    Parameter inch: a length in inches.
    Return: the length in centimeters.
    """

    cm = inch * 2.54
    
    return cm

def body_mass_index(weight, height):

    """Calculate and return a person's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
    Return: a person's body mass index.
    """
    bmi = weight / (height ** 2) * 10000

    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic rate (bmr).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
        age must be in years.
    Return: a person's basal metabolic rate in kcal per day.
    """

    if gender == "F":
        bmr = 447.593 + weight * 9.247  + height * 3.098  - 4.330 * age
            

    else:
        gender != "F"
        bmr = 88.362 + 13.397 * weight + 4.799  * height - 5.677 * age
          


    return bmr


# Call the main function so that
# this program will start executing.
main()

