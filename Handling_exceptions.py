# The following example code contains
# the outline of a complete try-except-else-finally
# block. Read the code and its comments carefully to 
# understand the correct syntax and organization of a try-except-else-finally block.

# Example 1

# try:
#     # Write normal code here. This block must include
#     # code that falls into two groups:
#     # 1. Code that may cause an exception to be raised
#     # 2. Code that depends on the results from the code
#     #    in the first group
# except ZeroDivisionError as zero_div_err:
#     # Code that the computer executes if the code in the
#     # try block caused a ZeroDivisionError to be raised.
# except ValueError as val_err:
#     # Code that the computer executes if the code in
#     # the try block caused a ValueError to be raised.
# except (TypeError, KeyError, IndexError) as error:
#     # Code that the computer executes if the code in the try
#     # block raised a TypeError, KeyError, or IndexError.
# except Exception as excep:
#     # Code that the computer executes if the code in the
#     # try block caused any exception to be raised that was
#     # not handled by one of the previous except blocks.
# except:
#     # Code that the computer executes if the code in the
#     # try block caused anything to be raised that was
#     # not handled by one of the previous except blocks.
# else:
#     # Code that the computer executes after the code
#     # in the try block if the code in the try block
#     # did not raise any exceptions.
# finally:
#     # Code that is executed after all the other code in
#     # try, except, and else blocks regardless of whether
#     # an exception was raised or not.


# The code in example 2 attempts to pass a string of text to the round function which 
# causes the computer to raise TypeError as shown in the output below the code example.

# Example 2

def main():
    print("TypeError")
    try:
        text = input("Please enter a number: ")
        integer = round(text)
        print(integer)

    except TypeError as type_err:
        print(type_err)

if __name__ == "__main__":
    main()


#  The code in example 3 and its output show a ValueError.
# Example 3

def main():
    print("ValueError")
    try:
        number = float(input("Please enter a number: "))
        print(number)

    except ValueError as val_err:
        print(val_err)

if __name__ == "__main__":
    main()

# The computer raises a ZeroDivisionError when a program attempts to divide a
# number by zero (0) as shown in example 4 and its output.

# Example 4

def main():
    print("ZeroDivisionError")
    try:
        players = int(input("Enter the number of players: "))
        teams = int(input("Enter the number of teams: "))

        players_per_team = players / teams

        print(f"Each team should have {players_per_team} players.")

    except ZeroDivisionError as zero_div_err:
        print(zero_div_err)

if __name__ == "__main__":
    main()

# IndexError
# Example 5

def main():
    print("IndexError")
    try:
        # Create a list that contains three family names.
        surnames = ["Smith", "Lopez", "Marsh"]

        # Attempt to change the surname at index 3. Because there
        # are only three names in the surnames list and therefore
        # the last index is 2, this statement will fail and cause
        # the computer to raise an IndexError.
        surnames[3] = "Olsen"

    except IndexError as index_err:
        print(index_err)

if __name__ == "__main__":
    main()


# Example 6

def main():
    try:
        # Create a list that contains three family names.
        surnames = ["Smith", "Lopez", "Marsh"]

        # Attempt to print the surname at index 3. Because there
        # are only three names in the surnames list and therefore
        # the last index is 2, this statement will fail and cause
        # the computer to raise an IndexError.
        print(surnames[3])

    except IndexError as index_err:
        print(index_err)

if __name__ == "__main__":
    main()

# KeyError
# Example 7

def main():
    print("KeyError")
    try:
        # Create a dictionary with student IDs as
        # the keys and student names as the values.
        students = {
            "42-039-4736": "Clint Huish",
            "61-315-0160": "Michelle Davis",
            "10-450-1203": "Jorge Soares",
            "75-421-2310": "Abdul Ali",
            "07-103-5621": "Michelle Davis"
        }

        # Attempt to find the key "50-420-1021",
        # which is not in the dictionary. This will
        # cause the computer to raise a KeyError.
        name = students["50-420-1021"]

        print(name)

    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

if __name__ == "__main__":
    main()

# FileNotFoundError
# Example 8

def main():
    print("FileNotFoundError")
    try:
        with open("products.vcs", "rt") as products_file:
            for line in products_file:
                print(line)

    except FileNotFoundError as not_found_err:
        print(not_found_err)

if __name__ == "__main__":
    main()


# PermissionError
# Example 9

def main():
    print("PermissionError")
    try:
        with open("contacts.csv", "rt") as contacts_file:
            for line in contacts_file:
                print(line)

    except PermissionError as perm_err:
        print(perm_err)

if __name__ == "__main__":
    main()