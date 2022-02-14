#!/usr/bin/env python3


from typing import List


def load_all_words(filename: str) -> List:

    with open(filename, mode="r") as file:
        all_words = [word.strip() for word in file.readlines()]

    return all_words


def wordle_word_list(word_list: List) -> List:

    wordle_words = [word for word in word_list if len(word) == 5]

    return wordle_words


def save_wordle_word_list(wordle_words: List, dest_loc: str) -> None:

    with open(dest_loc, mode="w") as file:
        file.write("\n".join(wordle_words))


if __name__ == "__main__":

    filename = "./assets/english-words.txt"
    dest_filename = "./assets/wordle-words.txt"

    word_list = load_all_words(filename)
    print("All Words Read")

    wordle_words = wordle_word_list(word_list)
    print("All 5 letter words picked")

    save_wordle_word_list(wordle_words, dest_filename)
    print("Data Written")
