import random

keep_playing = "yes"

while keep_playing == "yes":

    magic_number = random.randint(1, 10)

    guess = -1
    attempts = 0

    while guess != magic_number:
        guess = int(input("Guess the number> "))

        if guess < magic_number:
            print("Higher> ")
            attempts += 1
        elif guess > magic_number:
            print("Lower> ")
            attempts += 1
        else:
            print("You guessed right!")
            attempts += 1
            
    print(f"It took you {attempts} attempts!")
    input("Would you like to play again? (YES or NO)> ").lower()

