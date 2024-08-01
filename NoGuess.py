import random

guess_again = "Y"

while guess_again == "Y":
    def dice_function():
        dice_range = range(1, 6)
        value = random.choice(dice_range)
        return value

    def user_function():
        luckyguess = int(input("Guess a number between 1 and 6: "))
        if 1 <= luckyguess <= 6:
            return luckyguess
        else:
            print("Please enter a number between 1 and 6 ")

    if user_function() == dice_function():
        print("The number is" + str(dice_function()) + ". You got it! ")
    else:
        print("The number was " + str(dice_function()) + ". Better luck next time")

    guess_again = input("\nGuess again? Yes or No ")[0].upper()

print("Thank you for playing!")
