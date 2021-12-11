# Purpose
# Improve your understanding of calling built-in functions and functions that are in a standard Python module.
import math

# Problem Statement
# In our modern world economy, many items are manufactured in large factories, 
# then packed in boxes and shipped to distribution centers and retail stores.
# A common question for employees who pack items is "How many boxes do we need?"

# Assignment
# A manufacturing company needs a program that will help its employees pack manufactured 
# items into boxes for shipping. Write a Python program named
# boxes.py that asks the user for two integers:  1) the number of manufactured items 
# and 2) the number of items that the user will pack per box. Your program must
# compute and print the number of boxes necessary to hold the items. This must be a whole 
# number. Note that the last box may be packed with fewer items than the other boxes.

# Testing Procedure
# Verify that your program works correctly by following each step in this testing procedure:

# Run your program and enter the inputs shown in the Sample Run section below. 
# Ensure that your program's output matches the sample run output.

# Sample Runs
# > python boxes.py
# Enter the number of items: 8
# Enter the number of items per box: 5

# For 8 items, packing 5 items in each box, you will need 2 boxes.

# > python boxes.py
# Enter the number of items: 25
# Enter the number of items per box: 4

# For 25 items, packing 4 items in each box, you will need 7 boxes.

num_items = int(input("Enter the number of items:"))
items_per_box = int(input("Enter the number of items per box:"))

calculate =  num_items / items_per_box 

rounding = math.ceil(calculate)

print(f"For {num_items} items, packing {items_per_box}"
f" items in each box, you will need {rounding} boxes.")


