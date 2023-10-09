import random


secret_words = ['mosiah', 'nephi', 'helaman', 'alma', 'omni', 'lehi', 'moroni', 'sariah']

def display_hint(secret_word, guess):
    hint = ""
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper()
        elif guess[i] in secret_word:
            hint += guess[i].lower()
        else:
            hint += "_"
        hint += " "
    return hint.strip()

def play_game():
    secret_word = random.choice(secret_words).lower()
    num_guesses = 0
    guessed_word = "_" * len(secret_word)

    print("Welcome to Wordle!")
    print("Guess the word with", len(secret_word), "letters")

    while guessed_word != secret_word:
        print("\nHint:", " ".join(guessed_word.upper().split()))

        guess = input("Guess: ").lower()

        if len(guess) != len(secret_word):
            print("Invalid guess length. Please enter", len(secret_word), "letters.")
            continue

        num_guesses += 1

        if guess == secret_word:
            guessed_word = secret_word
        else:
            hint = display_hint(secret_word, guess)
            print("Hint:", hint)

    print("\nCongratulations! You correctly guessed the word '", secret_word.capitalize(), "'in", num_guesses, "guesses.")

if __name__ == "__main__":
    play_game()
