#!/usr/bin/env python3

import random
from typing import Dict, List
from dataclasses import dataclass
from logging import Logger


@dataclass
class WordleGame:
    wordle_file_loc: str
    tries: int
    logger: Logger

    def read_file(self) -> List:
        with open(self.wordle_file_loc, mode="r") as read_file:
            self.logger.debug("File Read")
            word_list = [word.strip() for word in read_file.readlines()]
        return word_list

    def choose_random_word(self, wordlist: List) -> str:
        word = random.choice(wordlist)
        self.logger.debug(f"Random Word Selected: {word}")
        return word

    def get_input(self, idx: int) -> str:

        while True:
            input_text = input(f"Enter 5 word guess (try {idx+1}) >>\n")
            self.logger.debug(f"Input Provided for {idx+1} try: {input_text}")

            if len(input_text) == 5 and input_text.isalpha():
                self.logger.debug(f"Input Selected for {idx+1} try: {input_text}")
                return input_text

    def add_to_dict(self, letter: str, dictionary: Dict) -> None:
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1

    def compare_words(self, input_word: str, chosen_word: str) -> List:

        input_word, chosen_word = input_word.lower(), chosen_word.lower()

        input_word_dict = dict()
        chosen_word_dict = {letter: chosen_word.count(letter) for letter in set(chosen_word)}
        self.logger.debug(f"Chosen Word Dict: {chosen_word_dict}")

        if input_word == chosen_word:
            return [1]

        compare_matrix, count = [], 0

        for letter1, letter2 in zip(input_word, chosen_word):
            self.logger.debug(f"Count: {count},Letter1: {letter1}, Letter2: {letter2}")

            self.add_to_dict(letter1, input_word_dict)
            self.logger.debug(f"Input Word Dict: {input_word_dict}")

            if letter1 == letter2:
                compare_matrix.append(2)

            elif input_word_dict[letter1] <= chosen_word_dict.get(letter1, 0):
                pos = chosen_word.find(letter1, count, 5)
                self.logger.debug(f"Pos Value: {pos}")
                if pos < 0:
                    pass
                elif input_word[pos] == letter1:
                    compare_matrix.append(0)
                    count += 1
                    continue
                compare_matrix.append(1)

            else:
                compare_matrix.append(0)

            count += 1

        return compare_matrix

    def colorize_word(self, input_word: str, compare_matrix: List) -> None:
        color_dict = {0: "\033[0m", 1: "\033[93m", 2: "\033[92m"}

        self.logger.debug(f"Input Word: {input_word}, Compare Matrix: {compare_matrix}")

        for letter, col in zip(input_word, compare_matrix):
            letter = letter.upper()
            print(f"{color_dict[col]}{letter}", end=" ")

        print(f"{color_dict[0]}")

    def start_game(self) -> bool:
        wordle_words = self.read_file()
        print("File Read")

        chosen_word = self.choose_random_word(wordle_words)
        print("Word Chosen")

        for i in range(self.tries):
            input_word = self.get_input(i)

            comp_mtrx = self.compare_words(input_word, chosen_word)

            if len(comp_mtrx) == 1:
                return True

            self.colorize_word(input_word, comp_mtrx)

        print(f"Correct word was : {chosen_word.upper()}")
        return False
