"""
Guess the Word Game

Algorithm:
1) Make a list of words
2) Choose a random word from the list  
3) Get a guess from user
4) Guess attempts = len(random word)
5) Check win/lose condition
"""

import random

# Make a list of words
colors = [
    "red", "blue", "green", "yellow", "orange", "pink", "purple", "brown",
    "black", "white", "gray", "violet", "indigo", "cyan", "magenta", "teal",
    "lime", "maroon", "navy", "olive", "silver", "gold", "beige", "coral",
    "turquoise", "peach", "lavender", "mint", "salmon", "chocolate", "tan"
]


def main():
    show_welcome_message()

    # Choose a random word from the list
    selected_word = random.choice(colors)

    # Allowed guess attempts = length of the selected word
    guess_count = len(selected_word)

    # Make a list of blank spaces for selected_word
    guessed_letters = ["-"] * guess_count

    # Show the user the number of spaces
    print(f"The word is => {unpack_list(guessed_letters)}")

    # Game Loop
    while guess_count > 0:
        # Get a char from user
        user_input = input("Enter your guess: ").lower().strip()

        # Process the guess and get result
        message, guess_count, guessed_letters, game_state = validate(
            user_input, guess_count, selected_word, guessed_letters)

        # Show appropriate message based on message
        print(message)

        # Check game state
        if game_state == "win":
            print("\n🔶 Congrats! You Won🥳 🔶\n")
            break
        elif game_state == "continue":
            continue
    else:
        print(f"\n🔷 You lost!😥 The answer was => {selected_word} 🔷\n")


def validate(user_input, guess_count, selected_word, guessed_letters):
    """
    Validate user's guess and return appropriate results.
    Returns: (message, new_guess_count, new_guess_list, game_state)
    game_state can be: "win", "lose", "continue"
    """

    # Check for non alphabetic input
    if not user_input.isalpha():
        return "Please enter only alphabetic characters!😩", guess_count, guessed_letters, "continue"

    # Check if user guessed the whole word
    if len(user_input) > 1:
        if user_input == selected_word:
            guessed_letters = list(selected_word)
            return f"Yesss! The word was indeed: {selected_word}", guess_count, guessed_letters, "win"
        else:
            # Wrong full-word guess, decrease attempt
            guess_count -= 1
            return f"Wrong guess for the whole word!😫 Remained guesses: {guess_count}", guess_count, guessed_letters, "continue"

    # Now user_input is guaranteed to be a single character
    if user_input in selected_word:
        # Check for duplicate char
        if user_input in guessed_letters:
            return "You entered this char before! Try a new one.🤨", guess_count, guessed_letters, "continue"
        # If it's a new correct char
        else:
            for idx, char in enumerate(selected_word):
                if char == user_input:
                    # Replace the char in guessed_letters
                    guessed_letters[idx] = user_input

            # Check if the word is complete
            # if unpack_list(guessed_letters) == unpack_list(selected_word):
            if "-" not in guessed_letters:
                return f"Correct! => {unpack_list(guessed_letters)}", guess_count, guessed_letters, "win"

            # Show the current guessed_letters to user
            return f"Correct! => {unpack_list(guessed_letters)}", guess_count, guessed_letters, "continue"

    # Wrong guess
    guess_count -= 1
    return f"Wrong!😫 => remained guesses: {guess_count}", guess_count, guessed_letters, "continue"


def unpack_list(guessed_letters):
    return " ".join(guessed_letters)


# Welcome message
def show_welcome_message():
    try:
        from colorama import init, Fore, Style
        init()
        
        print(Fore.CYAN + """
╔══════════════════════════════════════════════╗
║           🎲 Guess the Word Game 🎲          ║
╚══════════════════════════════════════════════╝""" + Style.RESET_ALL)
        
        print(Fore.BLUE + "\n Instruction: " + Style.RESET_ALL)
        print(Fore.RED +   "  🔴 I have picked a color from my colorful list. Can you guess it?" + Style.RESET_ALL)
        print(Fore.GREEN + "  🟢 You can either guess one letter at a time, or try to guess the whole word!" + Style.RESET_ALL)
        print(Fore.YELLOW +"  🟠 But be careful, your number of attempts is limited to the length of the word." + Style.RESET_ALL)
        
        print(Fore.CYAN + "\n" + "═"*50 + Style.RESET_ALL)
        print(Fore.BLUE + "🎯 GOOD LUCK! YOU'LL NEED IT!" + Style.RESET_ALL)
        print()
        
    except ImportError:
        # The simpler message
        print("\n🎨 Welcome to the 'Guess the Word Game'!🎨")


if __name__ == "__main__":
    main()
