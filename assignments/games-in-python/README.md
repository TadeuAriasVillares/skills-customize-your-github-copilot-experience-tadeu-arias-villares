
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build an interactive Hangman game in Python that uses strings, loops, conditionals, and user input to guess a hidden word.

## 📝 Tasks

### 🛠️ Create the game loop

#### Description
Write the main game loop that repeatedly asks the player to guess a letter, updates the displayed word state, and tracks remaining attempts until the game ends.

#### Requirements
Completed program should:

- randomly select a word from a predefined list
- prompt the player for a single letter guess each turn
- update and display the current word state in `_ _ _` format
- count and show incorrect guesses or remaining attempts

### 🛠️ Handle win/lose conditions

#### Description
Add logic to detect when the player has guessed the entire word or run out of attempts, then display the correct end-of-game message.

#### Requirements
Completed program should:

- stop when the player reveals all letters in the word
- stop when the player uses all allowed incorrect guesses
- print a win message with the full word when the player succeeds
- print a lose message and reveal the full word when the player fails
