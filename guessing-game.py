# Stupid yet another guessing game, why not
import random


lives = 5
secret = random.randint(0, 30)


while True:
    guess = int(input("Guess the number: "))
    if guess != secret:
        lives -= 1
        if lives == 0:
            print("Shit, try next time")
            break
        else:
            print(f"You have {lives} lives left.")
    else:
        print("yay")