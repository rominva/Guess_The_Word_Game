# guess the word Game
# a list of words
# choose a random word
# get a guess from user => check => win\lose

import random
countries = ["Germany", "America", "Australia", "England", "Austria", "France", "Italy"]

selected_word = random.choice(countries).lower()
print("Welcome to the \"Guess The Word\" game!🤩\nTry to guess the country's name.\nGood luck🧡")
word_list = ["-"] * len(selected_word)
print("the word is:", " ".join(word_list))

guess_attempt = len(selected_word)

while guess_attempt > 0:
    user_guess = input(
        "Enter your guess (a single letter or the whole word):\n")

    if user_guess in selected_word:
        if len(user_guess) == 1:
            if user_guess in word_list:
                print("you have gueesed this letter befor! please try a new one🙄")
            else:
                for idx, char in enumerate(selected_word):
                    if char == user_guess:
                        word_list[idx] = user_guess
                current_guess = "".join(word_list)
                print(f"perfect! => {current_guess}")

                if not "-" in word_list:
                    print(f"Congratulations🥳 You guessed the word: {
                          selected_word}")
                    break

        elif user_guess == selected_word:
            print(f"yes! the word was {selected_word}😎 you're a genious!")
            break
        else:
            guess_attempt -= 1
            print(f"wrong🤨 your remained attempts: {guess_attempt}")

    else:
        guess_attempt -= 1
        print(f"wrong! your remained attempts: {guess_attempt}")

else:
    print("sorry you have lost😓😢")
