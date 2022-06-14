import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)                          # saving letters in the word
    alphabet = set(string.ascii_uppercase)            # saving all uppercase letters
    used_letters = set()                              # save what the user has guessed

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        
        #letters used
        print("You have", lives, "lives left and you used these letters: ", " ".join(used_letters))

        #Current word: W O - D
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("The letter is not in the word.")

        elif user_letter in used_letters:
            print("You have already used the character. Please try again.")

        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("No lives remaining, better luck next time! The word was", word)
    else:
        print("Congratulations!!! You have guessed the word", word)

hangman()