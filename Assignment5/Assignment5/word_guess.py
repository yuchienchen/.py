"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """

    len(secret_word)
    secret_word.replace(symbol, "-") 

    print("The word now looks like this: " + "")
    print("You have " + INITIAL_GUESSES +  " guesses left")
    guess = "abcdefghijklmnopqrstuvwxyz"
    # guess.isalpha().lower()
    guess_count = INITIAL_GUESSES

    if guess == symbol:
        guess.replace("-", guess)

    for symbol in secret_word:
        while guess == input("Type a single letter here, then press enter: "):
            if guess.lower() == symbol:
                print("That guess is correct.")
                print("The word now looks like this: " + "")
                print("You have " + guess_count + " guesses left")
            if guess.lower() != symbol or guess.lower() is not guess.isalpha():
                guess_count -= 1
                print("There are no " + guess + " 's in the word")
                print("The word now looks like this: " + "")
                print("You have " + guess_count + " guesses left")
            if len(guess.lower()) >= 2:
                print("Guess should only be a single character.")
                print("The word now looks like this: " + "")
                print("You have " + guess_count + " guesses left")
                

    print("Congratulations, the word is: " + secret_word)
    print("Sorry, you lost. The secret word was: " + secret_word)


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    index = random.randrange(3)
    if index == 0:
        return 'HAPPY'
    elif index == 1:
        return 'PYTHON'
    else:
        return 'COMPUTER'


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()