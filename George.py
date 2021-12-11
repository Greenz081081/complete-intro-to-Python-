from tkinter.constants import S
import pytest




def main():
    print("welcome")

def get_difficulty():
    print("setting up")

    try:

        difficulty = "easy", "medium", "hard", "quit" 

        difficulty = input('Which difficulty would you like to play at? \n"Easy", "Medium", "Hard", or "quit" to exit>') 

    except ValueError as val_err: 
        print(f"Invalid entry: {difficulty}. Please try again.") 

        while difficulty.lower() != ("easy", "medium", "hard", "quit"):

            if difficulty.lower() == "quit": 
                            
                quit() 

            # else: 
                            
    return difficulty

main()