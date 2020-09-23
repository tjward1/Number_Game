# Taylor Ward
# Purpose: Create a number guessing game

# import random module to generate random number
import random

# generate random number (integer) between 1 & 100 inclusive
myNumber = random.randint(1, 100)

# print random number chosen so I can accurately assess my code
# do not want user to see, game would be no fun :(
#print(f"{myNumber}")

# initialize number of guesses
numGuess = 0

print("I'm thinking of a number between 1 and 100... Guess what it is!")
# ask for another guess as long as the guess is not correct
guess = ()
while guess != myNumber:
    # ask for user input
    guess = int(input("Your guess: "))
    # count the number of guesses
    numGuess += 1
    # allow the user to exit the game at any time by entering 0
    if guess == 0:
        print(f"\nSorry to see you go! My number was {myNumber}!")
        exit()
    elif guess > myNumber:
        print("Too high! Try again or enter 0 to quit")
    elif guess < myNumber:
        print("Too low! Try again or enter 0 to quit")
    # when user answers correctly, give number of guesses and exit the game
    else:
        print("\nThat's correct! Yay!")
        print(f"It only took you {numGuess} guesses!")