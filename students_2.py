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
        Id  = str(input("Please enter an I-Number (xxxxxxxxx):"))

        # uses the I-Number to find the corresponding student name in
        # the dictionary, and prints the name.
        if Id in students:
                value = students[Id]
                name = value[STUDENTS_NAME]
                print(name)
                
        # If a user enters an I-Number that doesn't exist in the 
        # dictionary, your program must print the message, "No such student" 
        # (without the quotes).        
        else:
                print("No such student")



def read_dict(filename, key_index):
    """Read the contents of a CSV file into a dictionary
    and return the dictionary.    

     Parameters
        filename: the name of the CSV file to read.
        key_index: the index of the line
            to use as the keys in the dictionary.
    Return: a dictionary that contains
        the contents of the CSV file.
    """

    students_file = {}
    # Opens the students.csv file for reading
    with open("students.csv", "rt") as csv_file:

    # Use the csv module to create a reader
    # object that will read from the opened file.
            reader = csv.reader(csv_file)  

    # skips the first line of text in the file because it contains only headings
            next(reader) 

    # reads the other lines of the file into a dictionary.
            for row in reader:

                key = row[key_index]
                students_file[key] = row

    return students_file

if __name__ == "__main__":
    main()



