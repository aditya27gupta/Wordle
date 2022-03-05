from typing import List, AnyStr, Tuple
import random


def read_file(file_loc: AnyStr) -> List:
    with open(file_loc, "r") as file_read:
        wordList = [word.strip() for word in file_read.readlines()]
    return wordList


def get_input() -> Tuple[str, str]:

    while True:
        input_text = input(f"Enter guessed word >>\n")
        if len(input_text) == 5 and input_text.isalpha():
            break

    while True:
        input_comp_matrix = input(f"Enter compare matrix >>\n")
        if len(input_comp_matrix) == 5 and input_comp_matrix.isdigit():
            break

    return input_text, input_comp_matrix


def wordle_word_check(input_word: str, comp_matrix: AnyStr, wordlist_word: str) -> bool:

    for i, (letter, num) in enumerate(zip(input_word, comp_matrix)):
        if num == "0" and letter in wordlist_word:
            count = 0
            for comp_num, word in zip(comp_matrix, input_word):
                if letter == word and comp_num == "0":
                    count += 1
            if not (input_word.count(letter) - count - wordlist_word.count(letter)):
                continue
            return False
        elif num == "1" and letter not in wordlist_word:
            return False
        elif num == "1" and letter == wordlist_word[i]:
            return False
        elif num == "2" and letter != wordlist_word[i]:
            return False

    return True


def get_game_input(file_loc: AnyStr, num_tries: int) -> None:
    wordlist = read_file(file_loc)
    for _ in range(num_tries):
        if not wordlist:
            print("No More Suggestions available")
            exit(0)
        input_word, matrix = get_input()
        if input_word in wordlist:
            wordlist.remove(input_word)
        for word in reversed(wordlist):
            if not wordle_word_check(input_word, matrix, word):
                wordlist.remove(word)

        random.shuffle(wordlist)
        print(f"Suggestion(s): {wordlist[:10]}")


if __name__ == "__main__":
    file_loc = "./assets/wordle-words.txt"
    num_tries = 6
    get_game_input(file_loc, num_tries)
