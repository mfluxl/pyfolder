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
    guess = input("What is your guess? ")
    attempt += 1 
    if guess == secret:
        print("congratulations! you guessed correctly!")
        KeepPlaying = "no"
        break
    elif guess != secret:
        if len(guess) < len(secret):
            print("Your guess had less letters than the word does!")
        if len(guess) > len(secret):
            print("Your guess had more letters than the word does!")
        print(f"{attempt} Attempt. Try again!")


