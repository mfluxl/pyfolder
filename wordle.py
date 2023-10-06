import random

#Extra mile: trying to make the code pick a random word from a list and display the underscores accordingly
#Using the random module

wordlist = ['mosiah', 'nephi', 'jacob', 'omni', 'helaman', 'alma', 'ether', 'moroni', 'jarom', 'enos']
secret = random.choice(wordlist)
KeepPlaying = "yes"
attempt = 0

print("welcome to the guessing game!")
print(f"Your hint is (the book of mormon): {len(secret) * '_ '} ")

while KeepPlaying == "yes":
    guess = input("What is your guess? ").lower()
    attempt += 1 
    if guess == secret:
        print("Congratulations! you guessed correctly!")
        KeepPlaying = "no"
        break
    elif guess != secret:
        if len(guess) < len(secret):
            print("Your guess has less letters than the word does!")
        if len(guess) > len(secret):
            print("Your guess has more letters than the word does!")
        print(f"{attempt} Attempt(s). Try again!")


