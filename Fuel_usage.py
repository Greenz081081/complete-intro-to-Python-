# Write a Python program named fuel_usage.py that asks the user for three numbers:

# A starting odometer value in miles
# An ending odometer value in miles
# An amount of fuel in gallons

# Your program must calculate and print fuel efficiency in both miles per gallon 
# and liters per 100 kilometers. Your program must have three functions named as follows:

# main
# miles_per_gallon
# lp100k_from_mpg

# All user input and printing must be in the main function. In other words, the
# miles_per_gallon and lp100k_from_mpg functions must not call the the input or
# print functions. To start your program, copy and paste the following code into your
# program and use it as a design as you write your program.
import math



def main():
    # Get an odometer value in U.S. miles from the user.

    # Get another odometer value in U.S. miles from the user.

    # Get a fuel amount in U.S. gallons from the user.
    text_odometer = input("Enter the first odometer reading (in miles):")
    text_second_odometer = input("Enter the second odometer reading (in miles):")
    text_amount = input("Enter the amount of fuel used (in gallons):")
    
    start_miles = float(text_odometer)
    end_miles = float(text_second_odometer)
    amount_gallons = float(text_amount)


    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.

    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.

    lp100k = lp100k_from_mpg(mpg)

    # Round the miles per gallon to one digit after the decimal.
    # rounded_mpg = round(mpg, 1)

    # Round the liters per 100 km to two digits after the decimal.
    # rounded_lp100k = round(lp100k, 2)

    # Display the results for the user to see.
    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")

    pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """

    mpg_calculation = (end_miles - start_miles) / amount_gallons

    return mpg_calculation


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    mpg_conversion = 235.215 / mpg

    return mpg_conversion


# Call the main function so that
# this program will start executing.
main()