import random
import re

# Lists of words for the game
easy_words = ["lion", "tiger", "horse", "bear", "rabbit",
             "koala", "panda", "snake", "otter", "raccoon"]
hard_words = ["kangaroo", "penguin", "cheetah", "dolphin", "chameleon",
             "platypus", "armadillo", "capybara", "fennec", "axolotl"]

# Function to display the hangman figure
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
    # Ask the player to choose between easy or hard mode
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

    # Choose a random word from the selected word list
    word = random.choice(words)

    # Initialize the variables
    guesses = ""
    max_attempts = 7

    # Initialize the hangman state
    hangman_state = 0

    # Display the initial hangman figure
    display_hangman(hangman_state)

    # Main game loop
    while max_attempts > 0:
        # Initialize the display word
        display_word = ""

        # For each letter in the word
        for letter in word:
            if letter in guesses:
                display_word += letter  # The letter has been guessed
            else:
                display_word += "_ "  # The letter is not guessed yet

        # Print the current state of the word
        print(display_word)

        # Ask the player to guess a letter
        while True:
            guess = input("Guess a letter: ").lower()
            if re.match("^[a-z]$", guess) and guess not in guesses:
                break
            elif guess in guesses:
                print("You've already guessed that letter!")
            else:
                print("Invalid input. Please enter a single letter.")

        # Add the guess to the list of guesses
        guesses += guess

        # Check if the guess is correct
        if guess not in word:
            max_attempts -= 1
            print(f"Wrong guess! {max_attempts} attempts left.")
            hangman_state += 1

        # Display the hangman figure
        display_hangman(hangman_state)

        # Check if the player has won
        if set(word).issubset(set(guesses)):
            print(f"Congratulations {player_name}! You guessed the word: {word}")
            return True  # Return True for a win

    # If the player has used all attempts
    if max_attempts == 0:
        print(f"Out of attempts! The word was: {word}")
        print(f"Sorry. {player_name}.")
        return False  # Return False for a loss

# Welcome the player and ask for their name
player_name = input("What's your name? ")
print(f"Hi {player_name}, welcome to Hangman!")

# Initialize win and loss counters
wins = 0
losses = 0

# Main game loop with restart option
while True:
    if play_hangman():
        wins += 1
    else:
        losses += 1

    # Display win and loss counters
    print(f"Total Wins: {wins}, Total Losses: {losses}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print(f"Thank you for playing, {player_name}! Goodbye.")
        break
