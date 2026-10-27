
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a playable Hangman game in Python. Practice string manipulation, loops, conditionals, user input, and random selection while managing the state of a game.

## 📝 Tasks

### 🛠️ Build the Game Setup

#### Description

Complete the setup for the Hangman game using the provided list of words and the `random` module. Create the variables needed to store the secret word, guessed letters, incorrect guesses, and the maximum number of incorrect guesses.

#### Requirements

Completed program should:

- Select one word at random from the provided `words` list.
- Initialize an empty collection for the player's guessed letters.
- Set a maximum number of incorrect guesses and track the current count.

### 🛠️ Implement the Guessing Game

#### Description

Implement the main game loop so the player can guess letters until they reveal the secret word or use all available incorrect guesses.

#### Requirements

Completed program should:

- Display the current progress of the secret word, showing unknown letters as underscores.
- Ask the player for a letter and update the game state based on whether the guess is correct.
- Track incorrect guesses and stop the game when the maximum is reached.
- End when the player reveals the entire word or runs out of attempts.
- Display a clear win or lose message at the end of the game.
