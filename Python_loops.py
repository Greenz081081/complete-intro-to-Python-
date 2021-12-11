# Example 4 shows three for loops that iterate over 
# a range of numbers. Notice that just like if statements
# in Python, the body of a loop starts and ends with indentation.


# Example 4

def main():
    # Count from zero to nine by one.
    print("Example 4")
    for i in range(10):
        print(i)
    print()

    # Count from zero to eight by two.
    for i in range(0, 10, 2):
        print(i)
    print()

    # Count from 100 down to 70 by three.
    for i in range(100, 69, -3):
        print(i)
    print()


# Call main to start this program.
if __name__ == "__main__":
    main()



# The for loop in example 5 uses underscore (_) 
# the counting variable, which is a valid variable
# name in Python. Many Python programmers use underscore 
# as the name of the counting variable to indicate that 
# the counting variable will not be used within the body of the loop.

# Example 5

def main():
    print("Example 5")
    sum = 0

    # Get ten or fewer numbers from the user and
    # add them together.
    for _ in range(10):
        number = float(input("Please enter a number: "))
        if number == 0:
            break
        sum += number

    # Print the sum of the numbers for the user to see.
    print(f"sum: {sum}")
    print()


# Call main to start this program.
if __name__ == "__main__":
    main()


# Example 6

def main():
    print("Example 6")
    # Create a list.
    colors = ["red", "orange", "yellow", "green", "blue"]

    # Use a for loop to print each element in the list.
    # Of course, the code in the body of a loop can do
    # much more with each element than simply print it.
    for color in colors:
        print(color)
    print()


# Call main to start this program.
if __name__ == "__main__":
    main()


# Example 7

import random


def main():
    print("Example 7")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")
    print()

    # Prepare a string that the input function will show to
    # the user during the first iteration of the while loop.
    prompt = "Please enter an integer between 1 and 100: "

    # Get a random integer between 1 and 100.
    answer = random.randint(1, 100)

    guess = -1
    attempts = 0

    while guess != answer:
        # Get a guess from the user.
        guess = int(input(prompt))
        attempts += 1

        # Compare the user's guess to the answer.
        if guess < answer:
            guide = "low"
        elif guess > answer:
            guide = "high"

        # Prepare a string that the input function will show to
        # the user during the next iteration of the while loop.
        prompt = f"{guess} is too {guide}. Please enter another integer: "

    print()
    print(f"{guess} is correct!")
    print(f"You used {attempts} guesses to guess the number.")
    print()


# Call main to start this program.
if __name__ == "__main__":
    main()


