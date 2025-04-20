from words import words

import random

# words = ["bear", "fish", "boar", "wolf", "eagle", "tiger", "snake", "horse"]
fun_attempts = [
    "Oops! That's not it!",
    "Nope! Try again!",
    "Wrong guess",
    "Close, but not quite!",
    "Ah, not this one!",
    "Yikes! You're hanging in there!"
]

hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

def get_display_word(word, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in word)

def handle_guess(guess, word, guessed, wrong_guesses):
    if guess in word:
        guessed.append(guess)
        return True
    else:
        wrong_guesses.append(guess)
        return False

def handle_wrong_attempt(attempts_left):
    print(random.choice(fun_attempts))
    print(hangman_stages[6 - attempts_left])

def game():
    word = random.choice(words)
    guessed = []
    wrong_guesses = []
    max_attempts = 6
    attempts_left = max_attempts

    print("-" * 30)
    print(" Let's play a game of HANGMAN!")
    print("-" * 30)

    while True:
        print("\nWord:", get_display_word(word, guessed))
        print(f"Guessed letters: {' '.join(guessed)}")
        print(f"Wrong guesses: {' '.join(wrong_guesses)}")
        print(f"Remaining attempts: {attempts_left}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single letter.")
            continue

        if guess in guessed or guess in wrong_guesses:
            print(" You already guessed that letter.")
            continue

        if not handle_guess(guess, word, guessed, wrong_guesses):
            attempts_left -= 1
            handle_wrong_attempt(attempts_left)

        if all(letter in guessed for letter in word):
            print("\n You WON! The word was:", word)
            
            break

        if attempts_left == 0:
            print(hangman_stages[-1])
            print("\n You LOST! The word was:", word)
            break

# Run the game
while True:
    game()
    again = input("\nPlay again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break
