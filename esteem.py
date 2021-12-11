def main():

    choice = ["D", "d", "a", "A"]
    score  = 0

    print("1. I feel that I am a person of worth, at least on an equal plane with others.")
    user_input_1 = input("Enter D, d, a, or A:")
    print("2. I feel that I have a number of good qualities.")
    user_input_2 = input("Enter D, d, a, or A:")
    print("3. All in all, I am inclined to feel that I am a failure.")
    user_input = input("Enter D, d, a, or A:")
    score = calculate_negative_choice(user_input, score)
    print("4. I am able to do things as well as most other people.")
    user_input_4 = input("Enter D, d, a, or A:")
    print("5. I feel I do not have much to be proud of.")
    user_input_5 = input("Enter D, d, a, or A:")
    score = calculate_negative_choice(user_input_5, score)
    print("6. I take a positive attitude toward myself.")
    user_input_6 = input("Enter D, d, a, or A:")
    print("7. On the whole, I am satisfied with myself.")
    user_input_7 = input("Enter D, d, a, or A:")
    print("8. I wish I could have more respect for myself")
    user_input_8 = input("Enter D, d, a, or A:")
    score = calculate_negative_choice(user_input_8, score)
    print("9. I certainly feel useless at times.")
    user_input_9 = input("Enter D, d, a, or A:")
    score = calculate_negative_choice(user_input, score)
    print("10. At times I think I am no good at all.")
    user_input_10 = input("Enter D, d, a, or A:")
    score = calculate_negative_choice(user_input, score)
    print(score)

def calculate_negative_choice(user_input, score):
    A = 0
    a = 1
    d = 2
    D = 3
    if user_input == "D":
        score += D

    elif user_input == "d":
        score += d

    elif user_input == "a":
        score += a

    elif user_input == "A":
        score += A

    return score


# def calculate_positive_choice():

main()

