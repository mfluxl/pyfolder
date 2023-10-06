
answer = "no"

while answer == "no":
    answer = input("May I have a piece of candy? ")

print("thanks")


#Printing the hidden favorite letter as an underscore:
""" 
word = "Uncopyrightable"
wordlen = len(word)

fav_letter = input("What is your favorite letter? >").lower()

for index in range(wordlen):
    letter = word[index]
    if letter == fav_letter:
        theletter = "_"
        print(theletter, end="")
    elif letter != fav_letter:
        print(letter, end="")
"""

# Printing the favorite letter capitalized:
"""

word = "Commitment"
wordlen = len(word)

fav_letter = input("What is your favorite letter? >").lower()

for index in range(wordlen):
    letter = word[index]
    if letter == fav_letter:
        theletter = letter.capitalize()
        print(theletter, end="")
    elif letter != fav_letter:
        print(letter, end="")
"""


# Printing the letter and its index:
"""
word = "nook"
num_letters = 4

for items in range(num_letters):
    letter = word[items]
    print(f'Letter: {letter} Number: {items}')
    print(f"The length of the word is {len(word)}"
          
"""
