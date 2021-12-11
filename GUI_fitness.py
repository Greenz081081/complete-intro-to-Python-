import tkinter as tk
import fitness_num_entry as numy
from tkinter import *
from datetime import datetime


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



def compute_age(birth):
    """Compute and return a person's age in years.
    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = (datetime.strptime(birth, "%Y-%m-%d"))
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


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and each
# widget is an object, the code to make a GUI usually has many variables
# to store the many objects. Because there are so many variable names,
# programmers often adopt a naming convention to help a programmer keep
# track of all the variables. One popular naming convention is to type a
# three letter prefix in front of the names of all variables that store
# GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main window
    Return: nothing
    """
    # Create labels for displays 
    lbl_gender = tk.Label(frm_main, text="Gender (M / F):")
    lbl_birthdays = tk.Label(frm_main, text="Birthdate (YYYY-MM-DD):")
    lbl_weighted_pounds = tk.Label(frm_main, text="Weight in Pounds:")
    lbl_heighted_inches = tk.Label(frm_main, text="Height in inches:")

    # Create a string entry box where the user will enter her gender.
    ent_gender = Entry(frm_main, width=5)
    ent_birthday = Entry(frm_main, width=10)
    ent_weight_pounds = Entry(frm_main, width=5)
    ent_height_inches = numy.IntEntry(frm_main, 1, 90, width=5)

     # Create a label that displays "Weight in pounds:"
    lbl_age_text = tk.Label(frm_main, text="Age (years):")
    lbl_kg_text = tk.Label(frm_main, text="Weight (kg):")
    lbl_cm_text = tk.Label(frm_main, text="Height (cm):")
    lbl_bmi_text = tk.Label(frm_main, text="Body mass index:")
    lbl_bmr_text = tk.Label(frm_main, text="Basal metabolic rate (kcal / day):")

    # Create labels that will display the results.
    the_birthday = tk.Label(frm_main, width=4)
    the_weight_pounds = tk.Label(frm_main, width=4)
    the_height_inches = tk.Label(frm_main, width=4)
    the_kg = tk.Label(frm_main, width=4)
    the_cm = tk.Label(frm_main, width=4)
    


    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_gender.grid(  row=0, column=0, padx=3, pady=3)
    ent_gender.grid(  row=0, column=1, padx=3, pady=3)
    lbl_birthdays.grid( row=1, column=0, padx=3, pady=3)
    ent_birthday.grid( row=1, column=1, padx=3, pady=3)
    lbl_weighted_pounds.grid(row=2, column=0, padx=3, pady=3)
    ent_weight_pounds.grid(row=2, column=1, padx=3, pady=3)
    lbl_heighted_inches.grid(row=3, column=0, padx=3, pady=3)
    ent_height_inches.grid(row=3, column=1, padx=3, pady=3)

    lbl_age_text.grid(row=0, column=2, padx=(30,3), pady=3)
    lbl_kg_text.grid(row=1, column=2, padx=(30,3), pady=3)
    lbl_cm_text.grid(row=2, column=2, padx=(30,3), pady=3)
    lbl_bmi_text.grid(row=3, column=2, padx=(30,3), pady=3)
    lbl_bmr_text.grid(row=4, column=2, padx=(30,3), pady=3)

    the_birthday.grid(row=0, column=3, padx=(30,3), pady=3)
    the_weight_pounds.grid(row=3, column=3, padx=(30,3), pady=3)
    the_height_inches.grid(row=4, column=3, padx=(30,3), pady=3)
    the_kg.grid(row=1, column=3, padx=(30,3), pady=3)
    the_cm.grid(row=2, column=3, padx=(30,3), pady=3)
    


    btn_clear.grid(row=4, column=0, padx=3, pady=3, columnspan=5, sticky="W")

    def calc(event):

        try:
            gender = ent_gender.get().upper()
            birthdate = ent_birthday.get()
            weight_in_pounds = int(ent_weight_pounds.get())
            height_in_inches = ent_height_inches.get()

            age = compute_age(birthdate)
            kg = kg_from_lb(weight_in_pounds)
            cm = cm_from_in(height_in_inches)
            bmi = body_mass_index(kg, cm)
            bmr = basal_metabolic_rate(gender, kg, cm, age)

            the_birthday.config(text=f"{age:.0f}")
            the_kg.config(text=f"{kg:.2f}")
            the_cm.config(text=f"{cm:.1f}")
            the_weight_pounds.config(text=f"{bmi:.1f}")
            the_height_inches.config(text=f"{bmr:.0f}")

        except ValueError:
            the_birthday.config(text="")
            the_weight_pounds.config(text="")
            the_height_inches.config(text="")
            the_kg.config(text="")
            the_cm.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_birthday.delete(0, tk.END)
        ent_gender.delete(0, tk.END)
        ent_weight_pounds.delete(0, tk.END)
        ent_height_inches.delete(0, tk.END)
        the_birthday.config(text="")
        the_weight_pounds.config(text="")
        the_height_inches.config(text="")
        the_kg.config(text="")
        the_cm.config(text="")
        ent_birthday.focus()
        ent_gender.focus()
        ent_weight_pounds.focus()
        ent_height_inches.focus()


    # Bind the calc function to the age entry box so
    # that the calc function will be called when the
    # user changes the text in the entry box.
    ent_birthday.bind("<KeyRelease>", calc)
    ent_gender.bind("<KeyRelease>", calc)
    ent_weight_pounds.bind("<KeyRelease>", calc)
    ent_height_inches.bind("<KeyRelease>", calc)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_birthday.focus()
    ent_gender.focus()
    ent_weight_pounds.focus()
    ent_height_inches.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()

