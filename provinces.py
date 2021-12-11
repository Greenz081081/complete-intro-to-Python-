# Write a Python program named provinces.py that reads the contents of 
# provinces.txt into a list and that modifies the list.

def main():
    # Read the contents of the file into a list where each
    # line of text in the file is stored in a separate element in the list.
    file_list = read_list("province.txt")


    # Print the entire list.
    print(file_list)
    print()

    # Remove the first element from the list.
    file_list.pop(0)

    # Remove the last element from the list.
    file_list.pop()

    # Replace all occurrences of "AB" in the list with "Alberta".
    for i in range(len(file_list)):
        if file_list [i] == "AB":
            file_list [i] = "Alberta"

    # Count the number of elements that are "Alberta" and print that number.
    count = file_list.count("Alberta")
    print(f"Alberta occurs {count} times in the modified list.")



    
 
def read_list(filename):
    """Read the contents of a text file into a list
    and return the list that contains the lines of text.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    file_list = []

    # Open the provinces.txt file for reading.
    with open("provinces.txt", "rt") as province_file:

        for elements in province_file:

    # Remove white space, if there is any,
    # from the beginning and end of the line.
            clean_white_space = elements.strip()

    
    # Append the clean line of text
    # onto the end of the list.
            file_list.append(clean_white_space)

    return file_list

if __name__ == "__main__":
    main()


