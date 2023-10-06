import random

min_number = 1
max_number = 10

def guess_my_number():
    global min_number, max_number
    magic_number = random.randint(min_number, max_number)
    guesses = 0

    print(f"guess a number between {min_number} and {max_number}")

    while True:
        guess = int(input("Guess the number> "))
        guesses += 1

        if guess == magic_number:
            print("congrats! you win.")
            break
        elif guess < magic_number:
            print("try a bigger number> ")
        else:
            print("try a lower number> ")
    
while True:
    guess_my_number()
    play_again = input("Do you want to play again? [Y/N]: ").lower()
    if play_again != "y":
        print("See you next time!")
        break