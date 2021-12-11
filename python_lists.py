# Example 1 contains a program that creates a list, 
# changes one item in the list, and then prints the entire list.

# Example 1

def main():
    # Create a list that contains five words.
    colors = ["yellow", "red", "green", "yellow", "blue"]

    # Print the length of the list.
    length = len(colors)
    print(length)

    # Print the element that is stored
    # at index 2 in the colors list.
    print(colors[2])

    # Change the element that is stored at
    # index 3 from "yellow" to "purple".
    colors[3] = "purple"

    # Print the entire colors list.
    print(colors)


# Call main to start this program.
if __name__ == "__main__":
    main()