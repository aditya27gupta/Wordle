#!/usr/bin/env python3

import random
from typing import Dict, List
from dataclasses import dataclass


@dataclass
class WordleGame:
    wordle_file_loc: str
    tries: int

    def read_file(self) -> List:
        with open(self.wordle_file_loc, mode="r") as read_file:
            word_list = [word.strip() for word in read_file.readlines()]
        return word_list

    def choose_random_word(self, wordlist: List) -> str:
        word = random.choice(wordlist)
        return word

    def add_to_dict(self, letter: str, dictionary: Dict) -> None:
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1

    def compare_words(self, input_word: str, chosen_word: str) -> List:

        input_word_dict = dict()
        chosen_word_dict = {letter: chosen_word.count(letter) for letter in set(chosen_word)}

        if input_word == chosen_word:
            return [1]

        compare_matrix, count = [], 0

        for letter1, letter2 in zip(input_word, chosen_word):

            self.add_to_dict(letter1, input_word_dict)

            if letter1 == letter2:
                compare_matrix.append(2)

            elif input_word_dict[letter1] <= chosen_word_dict.get(letter1, 0):
                pos = chosen_word.find(letter1, count, 5)

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

        for letter, col in zip(input_word, compare_matrix):
            letter = letter.upper()
            print(f"{color_dict[col]}{letter}", end=" ")

        print(f"{color_dict[0]}")

    def start_game(self) -> bool:
        wordle_words = self.read_file()
        print("File Read")

        chosen_word = self.choose_random_word(wordle_words )
        print("Word Chosen")

        for i in range(self.tries):
            input_word = input(f"Enter input (Try {i+1})>>\n")

            comp_mtrx = self.compare_words(input_word, chosen_word)

            if len(comp_mtrx) == 1:
                return True

            self.colorize_word(input_word, comp_mtrx)

        print(f"Correct word was : {chosen_word.upper()}")
        return False
