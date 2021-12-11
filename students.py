# Write a Python program named students.py that does the following

import csv

from os import name



def main():

 

        STUDENTS_ID_NUMBER_INDEX = 0

        STUDENTS_NAME = 1

             

        # Read the contents of a csv file

        # named students.csv into a dictionary.

        students = read_dict("students.csv", STUDENTS_ID_NUMBER_INDEX )  



        # Gets an I-Number from the user

        I_number  = str(input("Please enter an I-Number (xxxxxxxxx):"))

        I_number  = I_number.replace("-", "")

        if not I_number.isdigit():
            print("Invalid character in I-Number")

        elif len(I_number) < 9:
            print("Invalid I_number: to few digits")

        elif len(I_number) > 9:
            print("Invalid I-Number: too many digits")


        # uses the I-Number to find the corresponding student name in

        # the dictionary, and prints the name.

        if I_number in students:

                value = students[I_number]

                name = value[STUDENTS_NAME]

                print(name)

               

        # If a user enters an I-Number that doesn't exist in the

        # dictionary, your program must print the message, "No such student"

        # (without the quotes).        

        else:

                print("No such student")



def read_dict(filename, key_index):

    dict = {}

    with open("students.csv", "rt") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            key = row[key_index]

            dict[key] = row

    return dict

if __name__ == "__main__":
    main()