# Import the math module so I can use the math.pi and math.sqrt
import math

# Print a description of this program for the user to see
print("This program computes and outputs the")
print("surface area of a right circular cone")

# Get user input
print()
radius = float(input("Enter the radius of the cone:"))
hieght = float(input("Enter the hieght of the cone:"))

# Conpute the surface area of the cone
radical = math.sqrt(radius ** 2 + hieght ** 2)
surface_area = math.pi * radius * (radius + radical)

# Display the result to the user
print()
print(f"The surface area is {surface_area:.2f}")