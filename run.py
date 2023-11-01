import random

# lists of words
easy_words = ["lion", "tiger", "horse", "bear", "rabbit", "koala", "panda", "snake", "otter", "raccoon"]
hard_words = ["kangaroo", "penguin", "cheetah", "dolphin", "chameleon", "platypus", "armadillo", "capybara", "fennec", "axolotl"]

# function for displaying hangman
def display_hangman(hangman_state):
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

# Function to play the Hangman game
def play_hangman():

# Welcome the player and ask for their name
player_name = input("What's your name? ")
print(f"Hi {player_name}, welcome to Hangman!")