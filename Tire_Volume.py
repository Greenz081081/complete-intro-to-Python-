# The size of a car tire in the United States is represented with 
# three numbers like this: 205/60R15. The first number is the width 
# of the tire in millimeters. The second number is the aspect ratio. 
# The third number is the diameter in inches of the wheel that
# the tire fits. The volume of space inside a tire can be approximated with 


# Write a Python program named tire_volume.py that reads from the keyboard
# the three numbers for a tire and computes and outputs the volume of space inside that tire.


# v is the volume in liters,
# π is the constant PI which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
# w is the width of the tire in millimeters,
# a is the aspect ratio of the tire, and
# d is the diameter of the wheel in inches.


import math

# Gets the current date from the computer's clock.

from datetime import datetime

current_date_and_time = datetime.now(tz = None)

width = None
ratio = None
diameter = None
user_choice = "yes"
user_phone = ""

# Get input from the user

text_width = input("Enter the width of the tire in mm (ex 205):")
text_ratio = input("Enter the aspect ratio of the tire (ex 60):")
text_diameter = input("Enter the diameter of the wheel in inches (ex 15):")

# Convert user input from string to number 

width = float(text_width)
ratio = float(text_ratio)
diameter = float(text_diameter)

# Find tire prices for four or more tire sizes online. Add a set of if … elif … else
# statements in your program that use the tire width, tire aspect ratio, and wheel
# diameter that the user enters to find a price and then print the price.

if width == 205 and ratio == 60 and diameter == 15:
    # Calculate results
    radical = math.pi * width ** 2 * ratio
    volume = radical * (width * ratio + 2540 * diameter) / 10000000000
    final_answer = volume
    print(f"The approximate volume is {final_answer:.2f} liters.")
    price = "80,000.00"
    print(f"The price is: ${price:}")

elif width == 185 and ratio == 50 and diameter == 14:
    # Calculate results
    radical = math.pi * width ** 2 * ratio
    volume = radical * (width * ratio + 2540 * diameter) / 10000000000
    final_answer = volume
    print(f"The approximate volume is {final_answer:.2f} liters.")
    price = "45,000.00"
    print(f"The price is: ${price:}")

elif width == 225 and ratio == 70 and diameter == 15:
    # Calculate results
    radical = math.pi * width ** 2 * ratio
    volume = radical * (width * ratio + 2540 * diameter) / 10000000000
    final_answer = volume
    print(f"The approximate volume is {final_answer:.2f} liters.")
    price = "85,000.00"
    print(f"The price is: ${price:}")

elif width == 235 and ratio == 55 and diameter == 18:
    # Calculate results
    radical = math.pi * width ** 2 * ratio
    volume = radical * (width * ratio + 2540 * diameter) / 10000000000
    final_answer = volume
    print(f"The approximate volume is {final_answer:.2f} liters.")
    price = "49,000.00"
    print(f"The price is: ${price:}")

elif width == 275 and ratio == 40 and diameter == 20:
    # Calculate results
    radical = math.pi * width ** 2 * ratio
    volume = radical * (width * ratio + 2540 * diameter) / 10000000000
    final_answer = volume
    print(f"The approximate volume is {final_answer:.2f} liters.")
    price = "155,000.00"
    print(f"The price is: ${price:}")

else:
    print("Invalid!!!")


# After your program prints the tire volume to the terminal, your program should
# ask the user if she wants to buy tires with the dimensions that she entered.

user_choice = input("Do you want to buy tires with the dimensions you have entered:")

# If the user answers "yes", your program should ask for her phone number and store
# her phone number in the volumes.txt file.

if user_choice == "yes":
    user_phone = input("Please Enter Your Phone Number:")
    print("Number Successfully Added !!")

else:
    print("Thanks !!")

# Opens a text file named volumes.txt for appending

with open("Volume.txt", "at") as volume_file:

# Appends to the end of the volumes.txt file one line of text that contains the
# following five values:
# current date
# width of the tire
# aspect ratio of the tire
# diameter of the wheel
# volume of the tire

    print(user_phone, file=volume_file)
    print(f"{current_date_and_time:%Y-%m-%d}, {width:.0f}, {ratio:.0f}, {diameter:.0f}, {volume:.2f}", file=volume_file)

end = input("")







