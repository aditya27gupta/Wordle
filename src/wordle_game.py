#!/usr/bin/env python3

import random
from typing import List
from dataclasses import dataclass
from logging import Logger


@dataclass
class WordleGame:
    wordle_file_loc: str
    tries: int
    logger: Logger

    # Read method to get list of wordle words in a list
    def read_file(self) -> List:
        try:
            with open(self.wordle_file_loc, mode="r") as read_file:
                self.logger.debug("File Read")
                word_list = [word.strip() for word in read_file.readlines()]
            return word_list

        except Exception as ex:
            raise Exception(ex)

    # Function to get a random word out of list
    def choose_random_word(self, wordlist: List) -> str:
        try:
            word = random.choice(wordlist)
            self.logger.debug(f"Random Word Selected: {word}")
            return word

        except Exception as ex:
            raise Exception(ex)

    # Input method that validates input is a string and is of length 5
    def get_input(self, idx: int) -> str:
        try:
            while True:
                input_text = input(f"Enter 5 word guess (try {idx+1}) >>\n")
                self.logger.debug(f"Input Provided for {idx+1} try: {input_text}")

                if len(input_text) == 5 and input_text.isalpha():
                    return input_text

        except Exception as ex:
            raise Exception(ex)

    # Compare method to get comparison list based on position of letters in input and wordle word
    def compare_words(self, input_word: str, chosen_word: str) -> List:

        try:
            input_word, chosen_word = input_word.lower(), chosen_word.lower()
            cmp_matrix = []
            chosen_word_mark = {idx: False for idx, _ in enumerate(chosen_word)}

            for i, (letter1, letter2) in enumerate(zip(input_word, chosen_word)):
                check = True
                if letter1 == letter2:
                    cmp_matrix.append(2)
                    chosen_word_mark[i] = True

                elif letter1 in chosen_word:
                    for j, _ in enumerate(chosen_word):
                        if (
                            letter1 == chosen_word[j]
                            and input_word[j] != chosen_word[j]
                            and not chosen_word_mark[j]
                        ):
                            cmp_matrix.append(1)
                            chosen_word_mark[j] = True
                            check = False
                            break
                    if check:
                        cmp_matrix.append(0)
                else:
                    cmp_matrix.append(0)

                self.logger.debug(
                    f"Letter from Input: {letter1} and compare_matrix: {cmp_matrix}"
                )
                self.logger.debug(f"Chosen Word Letter Status: {chosen_word_mark}")

            return cmp_matrix

        except Exception as ex:
            raise Exception(ex)

    # Method to colorize the output based on comparison list
    def colorize_word(self, input_word: str, compare_matrix: List) -> None:
        try:
            color_dict = {0: "\033[0m", 1: "\033[93m", 2: "\033[92m"}

            self.logger.debug(
                f"Input Word: {input_word}, Compare Matrix: {compare_matrix}"
            )

            for letter, col in zip(input_word, compare_matrix):
                letter = letter.upper()
                print(f"{color_dict[col]}{letter}", end=" ")

            print(f"{color_dict[0]}")

        except Exception as ex:
            raise Exception(ex)

    # Method to start the game based on initialized input
    def start_game(self) -> bool:
        try:
            wordle_words = self.read_file()

            chosen_word = self.choose_random_word(wordle_words)

            for i in range(self.tries):
                input_word = self.get_input(i)
                comp_mtrx = self.compare_words(input_word, chosen_word)
                self.colorize_word(input_word, comp_mtrx)
                if set(comp_mtrx) == {
                    2,
                }:
                    return True

            print(f"Correct word was : {chosen_word.upper()}")
            return False

        except Exception as ex:
            raise Exception(ex)


if __name__ == "__main__":
    from log import get_logger

    logger = get_logger("TEST Compare Function")
    logger.disabled = True
    cls_obj = WordleGame("abc", 3, logger)
    output = cls_obj.compare_words("syste", "tyise")
    print(output)
