
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
# Convert user input from string to number 

width = float(input("Enter the width of the tire in mm (ex 205):"))
ratio = float(input("Enter the aspect ratio of the tire (ex 60):"))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15):"))
print()


# Find tire prices for four or more tire sizes online. Add a set of if … elif … else
# statements in your program that use the tire width, tire aspect ratio, and wheel
# diameter that the user enters to find a price and then print the price.

if width == 205 and ratio == 60 and diameter == 15:
    # Calculate results
    radical = math.pi * width ** 2 * ratio
    volume = radical * (width * ratio + 2540 * diameter) / 10000000000
    final_answer = volume
    price = "80,000.00"
    print(f"The approximate volume is {final_answer:.2f} liters.")
    print(f"The price is: ${price:}")

elif width == 215 and ratio == 50 and diameter == 13:
    # Calculate results
    radical = math.pi * width ** 2 * ratio
    volume = radical * (width * ratio + 2540 * diameter) / 10000000000
    final_answer = volume
    price = "45,000.00"
    print(f"The approximate volume is {final_answer:.2f} liters.")
    print(f"The price is: ${price:}")

elif width == 185 and ratio == 50 and diameter == 45:
    # Calculate results
    radical = math.pi * width ** 2 * ratio
    volume = radical * (width * ratio + 2540 * diameter) / 10000000000
    final_answer = volume
    price = "85,000.00"
    print(f"The approximate volume is {final_answer:.2f} liters.")
    print(f"The price is: ${price:}")

elif width == 165 and ratio == 80 and diameter == 13:
    # Calculate results
    radical = math.pi * width ** 2 * ratio
    volume = radical * (width * ratio + 2540 * diameter) / 10000000000
    final_answer = volume
    price = "49,000.00"
    print(f"The approximate volume is {final_answer:.2f} liters.")
    print(f"The price is: ${price:}")

elif width == 195 and ratio == 45 and diameter == 15:
    # Calculate results
    radical = math.pi * width ** 2 * ratio
    volume = radical * (width * ratio + 2540 * diameter) / 10000000000
    final_answer = volume
    price = "155,000.00"
    print(f"The approximate volume is {final_answer:.2f} liters.")
    print(f"The price is: ${price:}")

else:
    print("Unsecessful !!")


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