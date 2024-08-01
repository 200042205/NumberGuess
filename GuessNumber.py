import random


def dice_roll():
    value = range(1, 6)
    return random.choice(value)


def user_function():
    guess = int(input("Guess a number between 1 and 6: "))
    if 1 <= guess <= 6:
        return guess
    else:
        print("Sorry, guess between 1 and 6")
        return -1



guess_again = "y"
while guess_again == "y":
    user_number = user_function()
    print(user_number)
    comp_number = dice_roll()
    print(comp_number)
    if user_number == comp_number:
        print("Correct, The number was " + str(comp_number))
    else:
        print("Sorry, the number was " + str(comp_number))

    guess_again = input("Would you like to play again? (Y/N): ")[0].lower()

print("Thanks for playing!")
