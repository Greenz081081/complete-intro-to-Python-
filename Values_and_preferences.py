# In a Python program, the computer assigns
# values to variables differently based on their data type.
# Consider the small program in example 8 and the output of that program:



# Example 8

from typing import type_check_only


def main():
    print("Example 8")
    x = 17
    y = x
    print(f"Before changing x: x {x}  y {y}")
    x += 1
    print(f"After changing x:  x {x}  y {y}")

# Call main to start this program.
if __name__ == "__main__":
    main()


# The program in example 8 contains two integer
# variables named x and y. The program in example 8 does the following:

# The statement at line 11 stores the value 17 into the variable x.
# Line 12 copies the value that is in the variable x into the variable y.
# Line 13 prints the values of x and y which are both 17.
# Line 14 adds one to the value of x, making its value 18 instead of 17.
# Line 15 prints the values of x and y. The value of x was changed to 18. The value of y remained unchanged.

# Why did line 14 (x += 1) change the value of x but not change the value 
# of y? Because line 12 copied the value that was in x into y.



# Example 9 shows a small Python program that contains two variables named lx and ly that each refer to a list.
# This program is similar to the previous program, but it has two lists instead of two integers.

# Example 9

def main():
    print("Example 9")
    lx = [7, -2]
    ly = lx
    print(f"Before changing lx: lx {lx}  ly {ly}")
    lx.append(5)
    print(f"After changing lx:  lx {lx}  ly {ly}")

# Call main to start this program.
if __name__ == "__main__":
    main()


# (As to why there is a difference in the output of example 8 and 9,
# refer to the topic under list in my microsoft document)


# The fact that the computer copies the value of some data types (boolean, integer, float)
# and copies the reference for other data types (list and others) has important implications
# for passing arguments into functions. Consider the Python program in example 10 with two 
# functions named main and modify_args.

# Example 10

def main():
    print("Example 10")
    print("main()")
    x = 5
    lx = [7, -2]
    print(f"Before calling modify_args(): x {x}  lx {lx}")

    # Pass one integer and one list
    # to the modify_args function.
    modify_args(x, lx)

    print(f"After calling modify_args():  x {x}  lx {lx}")


def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters:
        n - A number
        alist - A list
    Return: nothing
    """
    print("   modify_args(n, alist)")
    print(f"   Before changing n and alist: n {n}  alist {alist}")

    # Change the values of both parameters.
    n += 1
    alist.append(4)

    print(f"   After changing n and alist:  n {n}  alist {alist}")


# Call main to start this program.
if __name__ == "__main__":
    main()



# From the output of example 10, we see that 
# modifying an integer parameter changes the 
# integer within the called function only.
# However, modifying a list parameter changes
# the list within the called function and within
# the calling function. Why? Because when a 
# computer passes a boolean, integer, or float 
# variable to a function, the computer copies the 
# value of that variable into the parameter of 
# the called function. However, when a computer passes 
# a list variable to a function, the computer copies 
# the reference so that the original variable and 
# the parameter both refer to the same value in memory.