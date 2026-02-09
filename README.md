# Guess the Word Game 🎨

A fun **Python word guessing game** where you try to guess a color by entering letters or the whole word.

![Version](https://img.shields.io/badge/version-7.0-blue)
![Python](https://img.shields.io/badge/python-3.x-green)

## 📺 Demo
![Guess the Word Demo](https://github.com/rominva/Guess_The_Word_Game/blob/main/assets/guess_the_word.gif)

## Algorithm

1. Create a list of words (colors).  
2. Randomly select a word from the list.  
3. Determine allowed guesses (`guess_count`) as the length of the selected word.  
4. Show the word as underscores (`-`) to indicate unguessed letters.  
5. Player enters a guess (either a single letter or the full word).  
6. Check the guess:  
   - If correct, reveal the letter(s) or win the game if the word is complete.  
   - If incorrect, decrease remaining attempts.  
7. Game ends when the word is fully guessed or attempts run out.  

---

## Features

- Supports guessing **letters** or the **whole word**.  
- Prevents repeated guesses of the same letter.  
- Friendly messages with emojis and colors (via `colorama`).  
- Guess attempts are equal to the length of the word.  
- Cross-platform: works even without `colorama`.  

---

## How to Play

1. Clone the repository or download the script.  
2. Install `colorama` (optional, for colored output):

```bash
pip install colorama
```

3. Run the Python script:

```bash
python guess_the_word.py
```

4. The program will display the word as underscores:

```bash
The word is => - - - - -
```

5. Enter a letter or the full word as your guess.

6. The program will give feedback:
• Correct letter: updates the underscores
• Wrong guess: decreases remaining attempts
• Duplicate letter: asks to try a new one

7. The game ends when you either guess the word correctly or run out of attempts.

##

## Requirements
• Python 3.x

• Optional: colorama for colored output
##
**Enjoy guessing the colors!** 🌈