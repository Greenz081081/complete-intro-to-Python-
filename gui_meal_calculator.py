import tkinter as tk
# import fitness_num_entry as numy
from tkinter import *
from datetime import datetime

current_date_and_time = datetime.now(tz = None)
def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Fitness")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)


    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    main_window(frm_main)

    # lbl_birthdate.config(text=f"{birth:.0f}")

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()




def compute_subtotal(cm, ca, cd, nc, am, aa, ad, na):
    subtotal_1 = (cm + ca + cd) * nc
    subtotal_2 = (am + aa + ad) * na
    Subtotal = subtotal_1 + subtotal_2

    return Subtotal

def compute_sales_tax(sub_t, sales_tr):
    sub_sales_tax = sub_t * (sales_tr / 100)
    sales_tax = sub_sales_tax

    return sales_tax

def compute_total(sub_t, sales_tr):
    sub_total = sub_t + sales_tr
    total = sub_total

    return total

def compute_change(pa, total):
    sub_change = pa - total
    change = sub_change

    return change




def main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main window
    Return: nothing
    """
    # Create labels for displays 
  
    lbl_child_meal = tk.Label(frm_main, text="What is the price of a child's meal:")
    lbl_adult_meal = tk.Label(frm_main, text="What is the price of an adult's meal:")
    lbl_child_appetizer = tk.Label(frm_main, text="What is the price of a child's appetizer:")
    lbl_child_drink = tk.Label(frm_main, text="What is the price of a child's drink:")
    lbl_adult_drink = tk.Label(frm_main, text="What is the price of an adult's drink:")
    lbl_adult_appetizer = tk.Label(frm_main, text="What is the price of an adult's appetizer:")
    lbl_number_of_children = tk.Label(frm_main, text="How many children are there:")
    lbl_number_of_adults = tk.Label(frm_main, text="How many adults are there:")
    lbl_sales_tax = tk.Label(frm_main, text="What is the sales tax rate:")
    lbl_payment_amount =tk.Label(frm_main, text="What is the payment amount:")
    
 
    # Create a string entry box where the user will enter the prices.
    ent_child_meal = Entry(frm_main, width=10)
    ent_adult_meal = Entry(frm_main, width=10)
    ent_child_appetizer = Entry(frm_main, width=10)
    ent_child_drink = Entry(frm_main, width=10)
    ent_adult_drink = Entry(frm_main, width=10)
    ent_adult_appetizer = Entry(frm_main, width=10)
    ent_number_of_children = Entry(frm_main, width=10)
    ent_number_adults = Entry(frm_main, width=10)
    ent_sales_tax = Entry(frm_main, width=10)
    ent_payment_amount =Entry(frm_main, width=10)
    



     # Create a label for displays. 
    lbl_subtotal_text = tk.Label(frm_main, text="Subtotal:")
    lbl_sales_text = tk.Label(frm_main, text="Sales Tax:")
    lbl_total_text = tk.Label(frm_main, text="Total:")
    lbl_change_text = tk.Label(frm_main, text="Change:")

 
  

    # Create labels that will display the results.
    the_subtotal = tk.Label(frm_main, width=6)
    the_sales_tax = tk.Label(frm_main, width=6)
    the_total = tk.Label(frm_main, width=6)
    the_change =tk.Label(frm_main, width=6)
    the_time = tk.Label(frm_main, width=20)
    
    


    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_child_meal.grid(row=0, column=0, padx=3, pady=3)
    ent_child_meal.grid(row=0, column=1, padx=3, pady=3)
    lbl_adult_meal.grid(row=1, column=0, padx=3, pady=3)
    ent_adult_meal.grid(row=1, column=1, padx=3, pady=3)
    lbl_child_appetizer.grid(row=2, column=0, padx=3, pady=3)
    ent_child_appetizer.grid(row=2, column=1, padx=3, pady=3)
    lbl_child_drink.grid(row=3, column=0, padx=3, pady=3)
    ent_child_drink.grid(row=3, column=1, padx=3, pady=3)
    lbl_adult_drink.grid(row=4, column=0, padx=3, pady=3)
    ent_adult_drink.grid(row=4, column=1, padx=3, pady=3)
    lbl_adult_appetizer.grid(row=5, column=0, padx=3, pady=3)
    ent_adult_appetizer.grid(row=5, column=1, padx=3, pady=3)
    lbl_number_of_children.grid(row=6, column=0, padx=3, pady=3)
    ent_number_of_children.grid(row=6, column=1, padx=3, pady=3)
    lbl_number_of_adults.grid(row=7, column=0, padx=3, pady=3)
    ent_number_adults.grid(row=7, column=1, padx=3, pady=3)
    lbl_sales_tax.grid(row=8, column=0, padx=3, pady=3)
    ent_sales_tax.grid(row=8, column=1, padx=3, pady=3)
    lbl_payment_amount.grid(row=9, column=0, padx=3, pady=3)
    ent_payment_amount.grid(row=9, column=1, padx=3, pady=3)
    




    lbl_subtotal_text.grid(row=0, column=2, padx=(30,3), pady=3)
    lbl_sales_text.grid(row=1, column=2, padx=(30,3), pady=3)
    lbl_total_text.grid(row=2, column=2, padx=(30,3), pady=3)
    lbl_change_text.grid(row=3, column=2, padx=(30,3), pady=3)
    
    


    the_subtotal.grid(row=0, column=3, padx=(30,3), pady=3)
    the_sales_tax.grid(row=1, column=3, padx=(30,3), pady=3)
    the_total.grid(row=2, column=3, padx=(30,3), pady=3)
    the_change.grid(row=3, column=3, padx=(30,3), pady=3)
    the_time.grid(row=5, column=2, padx=(30,3), pady=3 )

    
    


    btn_clear.grid(row=10, column=0, padx=3, pady=3, columnspan=5, sticky="W")

    def calc(event):

        try:
            childs_meal = float(ent_child_meal.get())
            adults_meal = float(ent_adult_meal.get())
            childs_appetizer = float(ent_child_appetizer.get())
            childs_drink = float(ent_child_drink.get())
            adults_drink = float(ent_adult_drink.get())
            adults_appetizer = float(ent_adult_appetizer.get())
            numbers_of_children = int(ent_number_of_children.get())
            numbers_of_adults = int(ent_number_adults.get())
            sales_tax = float(ent_sales_tax.get())
            payment_amount = float(ent_payment_amount.get())
           
          
            subtotal = compute_subtotal(childs_meal, childs_appetizer, childs_drink, numbers_of_children, adults_meal, adults_appetizer, adults_drink, numbers_of_adults)
            sales_tax_rate = compute_sales_tax(subtotal, sales_tax)
            total = compute_total(subtotal, sales_tax_rate)
            change = compute_change(payment_amount, total)
            

            the_subtotal.config(text=f"{subtotal:.2f}")
            the_sales_tax.config(text=f"{sales_tax_rate:.2f}")
            the_total.config(text=f"{total:.2f}")
            the_change.config(text=f"{change:.2f}")
            the_time.config(text=f"{current_date_and_time:%a %b %w %X %Y}")

            

        except ValueError:
            the_subtotal.config(text="")
            the_sales_tax.config(text="")
            the_total.config(text="")
            the_change.config(text="")
            
            

    
    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_child_meal.delete(0, tk.END)
        ent_adult_meal.delete(0, tk.END)
        ent_child_appetizer.delete(0, tk.END)
        ent_child_drink.delete(0, tk.END)
        ent_adult_drink.delete(0, tk.END)
        ent_adult_appetizer.delete(0, tk.END)
        ent_number_of_children.delete(0, tk.END)
        ent_number_adults.delete(0, tk.END)
        ent_sales_tax.delete(0, tk.END)
        ent_payment_amount.delete(0, tk.END)
        the_subtotal.config(text="")
        the_sales_tax.config(text="")
        the_total.config(text="")
        the_change.config(text="")
        the_time.config(text="")
        ent_child_meal.focus()
        ent_adult_meal.focus()
        ent_child_appetizer.focus()
        ent_adult_appetizer.focus()
        ent_child_drink.focus()
        ent_adult_drink.focus()
        ent_number_of_children.focus()
        ent_number_adults.focus()
        ent_sales_tax.focus()
        ent_payment_amount.focus()


    # Bind the calc function to the entry box so
    # that the calc function will be called when the
    # user changes the text in the entry box.
    ent_child_meal.bind("<KeyRelease>", calc)
    ent_adult_meal.bind("<KeyRelease>", calc)
    ent_child_appetizer.bind("<KeyRelease>", calc)
    ent_adult_appetizer.bind("<KeyRelease>", calc)
    ent_child_drink.bind("<KeyRelease>", calc)
    ent_adult_drink.bind("<KeyRelease>", calc)
    ent_number_of_children.bind("<KeyRelease>", calc)
    ent_number_adults.bind("<KeyRelease>", calc)
    ent_sales_tax.bind("<KeyRelease>", calc)
    ent_payment_amount.bind("<KeyRelease>", calc)
    

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_child_meal.focus()
    ent_adult_meal.focus()
    ent_child_drink.focus()
    ent_adult_drink.focus()
    ent_child_appetizer.focus()
    ent_adult_appetizer.focus()
    ent_number_of_children.focus()
    ent_number_adults.focus()
    ent_sales_tax.focus()
    ent_payment_amount.focus()
    


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()