import random

#Extra Mile: Using a list of words and automatically displaying the hints according to the word from the list

secret_words = ['mosiah', 'nephi', 'helaman', 'alma', 'abinadi', 'lehi', 'moroni', 'sariah']


secret_word = random.choice(secret_words).lower()
guessed_word = "_ " * len(secret_word)  

print("Guess the word with", len(secret_word), "letters.")

num_guesses = 0


while guessed_word != secret_word:
    print("\nHint:", " ".join(guessed_word.upper().split()))
    guess = input("Guess> ").lower()

    if len(guess) != len(secret_word):
        print("Invalid! Enter", len(secret_word), "letters.")
        continue

    num_guesses += 1

    if guess == secret_word:
        guessed_word = secret_word
    else:
        hint = ""
        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                hint += guess[i].upper()
            elif guess[i] in secret_word:
                hint += guess[i].lower()
            else:
                hint += "_"
            hint += " "
        guessed_word = hint.strip()
        print("Your hint is:", guessed_word)

print("\nCongratulations! You guessed the word '", secret_word.capitalize(), "'in", num_guesses, "guesses.")
