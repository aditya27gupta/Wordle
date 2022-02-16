#!/usr/bin/env python3

from wordle_game import WordleGame
from log import get_logger


if __name__ == "__main__":
    logger = get_logger(__name__)
    file_loc = "./assets/wordle-words.txt"
    tries = 6

    logger.debug(f"File Loc: {file_loc}")
    logger.debug(f"No of Tries: {tries}")

    game = WordleGame(file_loc, tries, logger)

    logger.debug("wordleGame Class Intantiated")

    check = game.start_game()

    logger.debug(f"Check variable value: {check}")

    if check:
        print("You have guessed the word correctly. Congrats !!")

    else:
        print("Sorry you couldn't guess the word correctly")
