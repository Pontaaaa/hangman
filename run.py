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
    play Hangman with user interaction.

    Returns:
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

    # randomly selected word from word list
    word = random.choice(words)

    # initialize the variables
    guesses = ""
    max_attempts = 7

    # initialize the hangman state
    hangman_state = 0

    # display the initial hangman
    display_hangman(hangman_state)

    # main game loop
    while max_attempts > 0:
        # initialize the display word
        display_word = ""

        # for the letters in the word
        for letter in word:
            if letter in guesses:
                display_word += letter  # The letter has been guessed
            else:
                display_word += "_ "  # The letter is not guessed yet

        # print the current state of the word
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

        # add the guess to the list of guesses
        guesses += guess

        # check if the guess is correct
        if guess not in word:
            max_attempts -= 1
            print(f"Wrong guess! {max_attempts} attempts left.")
            hangman_state += 1

        # display the hangman
        display_hangman(hangman_state)

        # check if player has won
        if set(word).issubset(set(guesses)):
            print(f"Congratulations {player_name}! You guessed the word: {word}")
            return True  # Return True for a win

    # if player has used all their attempts
    if max_attempts == 0:
        print(f"Out of attempts! The word was: {word}")
        print(f"Sorry. {player_name}.")
        return False  # Return False for a loss

# ask player for their name and welcome them
player_name = input("What's your name? ")
print(f"Hi {player_name}, welcome to Hangman!")

# initialize win and loss counters
WINS = 0
LOSSES = 0

# restart option
while True:
    if play_hangman():
        WINS += 1
    else:
        LOSSES += 1

    # display win and loss counters
    print(f"Total Wins: {WINS}, Total Losses: {LOSSES}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print(f"Thank you for playing, {player_name}! Goodbye.")
        break
