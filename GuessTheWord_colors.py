# name list
# choose a random name of the list
# guess_count = length of the word
# show to user: ----  & give a letter from user
# check show => feedback
# if guess_count>0 => win/lose

import random
words = ["pink", "blue", "green", "red", "black",
         "white", "purple", "yellow", "brown", "orange"]
selected_word = random.choice(words)

guess_count = len(selected_word)

word_letters = ["-"] * len(selected_word)
print(f"I chose the color \"{
      " ".join(word_letters)}\"🌈\nhmm, such a nice color😍")

while guess_count > 0:
    user_guess = input(
        "Guess a letter or the full word of the color: \n").lower()

    if user_guess.isalpha():
        if len(user_guess) == 1:  # Checking if the user entered a single letter guess
            if user_guess in selected_word:
                if user_guess in word_letters:
                    print("you have guessed this letter before! try a new one.")
                else:
                    for idx, char in enumerate(selected_word):
                        if char == user_guess:
                            word_letters[idx] = user_guess
                    print(f"yes that's right! => {"".join(word_letters)}")

                    if not "-" in word_letters:
                        if selected_word == "pink":
                            color = "💗"
                        elif selected_word == "red":
                            color = "💖"
                        elif selected_word == "blue":
                            color = "💙"
                        elif selected_word == "black":
                            color = "🖤"
                        elif selected_word == "orange":
                            color = "🧡"
                        elif selected_word == "yellow":
                            color = "💛"
                        elif selected_word == "green":
                            color = "💚"
                        elif selected_word == "purple":
                            color = "💜"
                        elif selected_word == "white":
                            color = "🤍"
                        elif selected_word == "brown":
                            color = "🤎"

                        print(f"you won!🥳 The color was {
                              selected_word}{color}")
                        break
            else:
                guess_count -= 1
                print(f"wrong! your remained guess: {guess_count}😥")

        # Checking if the user entered the full word guess
        elif len(user_guess) == len(selected_word) and user_guess == selected_word:
            print(f"Congratulations! You guessed the color: {selected_word}")
            break

        else:
            print("Wrong guess! Try again.")

    else:
        print("please enter a valid character!")

else:
    print(f"geme over😓 the color was: {selected_word}")
