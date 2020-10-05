# Stupid yet another guessing game, why not
import random
import cute_print


lives = 5
secret = random.randint(0, 15)

cute_print.cute_print()

while True:
    guess = int(input("Guess the number: "))

    # checking if the guess isn't right
    if guess != secret:
        lives -= 1
        if lives == 0:
            print("Shit, try next time")
            break
        else:
            print(f"You have {lives} lives left.")

    # if the guess is right, print that to the user
    else:
        print(f"yay, {secret} was the answer")