#!/usr/bin/env python3

from wordle_game import WordleGame


if __name__ == "__main__":
    file_loc = "./assets/wordle-words.txt"
    tries = 6

    game = WordleGame(file_loc, tries)

    check = game.start_game()

    if check:
        print("You have guessed the word correctly. Congrats !!")

    else:
        print("Sorry you couldn't guess the word correctly")
