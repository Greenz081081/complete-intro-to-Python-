# Improve your understanding of calling built-in functions and
#  functions and methods that are in a standard Python module.

# You work for a retail store that wants to increase sales on Tuesday and Wednesday,
# which are the store's slowest sales days. On Tuesday and Wednesday, if a customer's
# subtotal is $50 or greater, the store will discount the customer's subtotal by 10%.

# Write a Python program named discount.py that gets a customer's subtotal as input
# and gets the current day of the week from your computer's clock. Your program must
# not ask the user to enter the day of the week. Instead, it must get the day of the week
# from your computer's clock.

# If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program
# must subtract 10% from the subtotal. Your program must then compute the total
# amount due by adding sales tax of 6% to the subtotal. Your program must print the
# discount amount if applicable, the sales tax amount, and the total amount due.

# Your program asks the user for the subtotal but does not ask the user for the
# day of the week. Your program gets the day of the week from your computer's clock.

from datetime import datetime

current_date_and_time = datetime.now(tz = None)

day_of_week = current_date_and_time.weekday()


discount_rate = 0.10
sales_tax_rate = 0.06

final_choice = "done"

subtotal = None
# print(day_of_week)
# print(current_date_and_time)

while subtotal != final_choice:   
    text = input("Please enter the subtotal:")
    subtotal = float(text)
    
   

    if subtotal >= 50 and day_of_week == 0: 
        sales_tax = subtotal * 0.06
        total_amount_due = subtotal  + sales_tax
        print(f"Sales Tax Amount: {sales_tax:.2f} ")
        print(f"Total: {total_amount_due:.2f}")

    elif subtotal <= 50 and day_of_week == 0:
        sales_tax = subtotal * 0.06
        total_amount_due = subtotal  + sales_tax
        print(f"Sales Tax Amount: {sales_tax:.2f} ")
        print(f"Total: {total_amount_due:.2f}") 

    
 
    elif subtotal >= 50 and day_of_week != 0:
        discount = subtotal * discount_rate
        subtotal = subtotal - discount
        sales_tax = round(subtotal * 0.06, 2)
        total_amount_due = subtotal + sales_tax
        print(f"Discount: {discount:.2f}")
        print(f"Sales Tax Amount: {sales_tax}")
        print(f"Total: {total_amount_due:.2f}")


    elif subtotal <= 50 and day_of_week != 0:
        sales_tax = subtotal * 0.06
        total_amount_due = subtotal +  sales_tax
        print(f"Sales Tax Amount: {sales_tax:.2f}")
        print(f"Total: { total_amount_due:.2f}")



# INSTRUCTORS EXAMPLE

# # Import the datatime module so that
# # it can be used in this program.
# from datetime import datetime

# # The discount rate is 10% and the sales tax rate is 6%.
# DISC_RATE = 0.10
# SALES_TAX_RATE = 0.06

# # Get the subtotal from the user.
# text = input("Please enter the subtotal: ")
# subtotal = float(text)

# # Call the now() method to get the current date and
# # time as a datetime object from the computer's clock.
# current_date_and_time = datetime.now()

# # Call the weekday() method to get the day of the
# # week from the current_date_and_time object.
# weekday = current_date_and_time.weekday()

# # if the subtotal is greater than 50 and
# # today is Tuesday or Wednesday, compute the discount.
# if subtotal >= 50 and (weekday == 1 or weekday == 2):
#     discount = round(subtotal * DISC_RATE, 2)
#     print(f"Discount amount: {discount}")
#     subtotal -= discount

# # Compute the sales tax. Notice that we compute the sales tax
# # after computing the discount because the customer does not
# # pay sales tax on the full price but on the discounted price.
# sales_tax = round(subtotal * SALES_TAX_RATE, 2)
# print(f"Sales tax amount: {sales_tax}")

# # Compute the total by adding the subtotal and the sales tax.
# total = subtotal + sales_tax

# # Display the total for the user to see.
# print(f"Total: {total:.2f}")


    

   




