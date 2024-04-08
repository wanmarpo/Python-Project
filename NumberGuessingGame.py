# A number guessing game
import random

play = True

while play:
    number = random.randrange(1,10)

    while True:
        guess = int(input("Guess a number between 1 to 10: "))

        if guess < number:
            print("This number is too small")
        elif guess > number:
            print("This number is too big")
        else:
            break

    print("Congratulations! You guessed it right.")

    while True:
        playing = input("Do you want to play again?[y/n] ")

        if playing == "y":
            play = True
            break
        elif playing == "n":
            play = False
            break
        else:
            print("Enter y or n only!")

print("See you next time!")