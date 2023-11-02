"""
hangman game
"""

import random
import re

# lists of words for the game
easy_words = ["lion", "tiger", "horse", "bear", "rabbit",
             "koala", "panda", "snake", "otter", "raccoon"]
hard_words = ["kangaroo", "penguin", "cheetah", "dolphin", "chameleon",
             "platypus", "armadillo", "capybara", "fennec", "axolotl"]

# function to display the hangman
def display_hangman(hangman_state):
    """
    display the hangman based on the hangman_state.
    """
    hangman_parts = [
        "  +---+\n      |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
    ]

    print(hangman_parts[hangman_state])

# function to play the game
def play_hangman():
    """
    play hangman with user interaction.

    returns:
        bool: true if the player wins and false if the player loses.
    """
    while True:
        word_type = input("Choose game type (easy or hard): ").lower()
        if word_type == "easy":
            words = easy_words
            break
        elif word_type == "hard":
            words = hard_words
            break
        else:
            print("Invalid input. Please enter 'easy' or 'hard'.")

    # randomly select word from word list
    word = random.choice(words)

    # max guesses
    guesses = ""
    max_attempts = 7

    # initialize the hangman state
    hangman_state = 0

    display_hangman(hangman_state)

    # main game loop
    while max_attempts > 0:

        display_word = ""

        # for the letters in the word
        for letter in word:
            if letter in guesses:
                display_word += letter  # letter has been guessed
            else:
                display_word += "_ "  # letter is not guessed yet

        print(display_word)

        # guess the letter
        while True:
            guess = input("Guess a letter: ").lower()
            if re.match("^[a-z]$", guess) and guess not in guesses:
                break
            elif guess in guesses:
                print("You've already guessed that letter!")
            else:
                print("Invalid input. Please enter a single letter.")

        guesses += guess

        # check if the guess is correct
        if guess not in word:
            max_attempts -= 1
            print(f"Wrong guess! {max_attempts} attempts left.")
            hangman_state += 1

        display_hangman(hangman_state)

        # if player has won
        if set(word).issubset(set(guesses)):
            print(f"Congratulations {player_name}! You guessed the word: {word}")
            return True  # Return True for a win

    # if player has lost
    if max_attempts == 0:
        print(f"Out of attempts! The word was: {word}")
        print(f"Sorry. {player_name}.")
        return False  # Return False for a loss

# ask player for their name and welcome them
while True:
    player_name = input("What's your name? ")
    if re.match("^[a-zA-Z]*$", player_name):
        break
    else:
        print("Invalid. Please only use letters.")

print(f"Hi {player_name}, welcome to Hangman!")

# win, loss counters and restart option
WINS = 0
LOSSES = 0

while True:
    if play_hangman():
        WINS += 1
    else:
        LOSSES += 1

    print(f"Total Wins: {WINS}, Total Losses: {LOSSES}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print(f"Thank you for playing, {player_name}! Goodbye.")
        break
