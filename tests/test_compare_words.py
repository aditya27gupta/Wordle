import pytest

from src.wordle_game import WordleGame
from src.log import get_logger

logger = get_logger("TEST Compare Function")
logger.disabled = True


input_output = [
    ("aaaaa", "abcde", [2, 0, 0, 0, 0]),
    ("aaaaa", "bcdea", [0, 0, 0, 0, 2]),
    ("abcde", "bcdea", [1, 1, 1, 1, 1]),
    ("bcdea", "abcde", [1, 1, 1, 1, 1]),
    ("aabbc", "abcde", [2, 0, 1, 0, 1]),
    ("abcde", "aabbc", [2, 1, 1, 0, 0]),
]


@pytest.mark.parametrize("input_word, chosen_word, output", input_output)
def test_compare_test(input_word, chosen_word, output):

    file_loc = "example.txt"
    tries = 6

    class_object = WordleGame(file_loc, tries, logger)

    result = class_object.compare_words(input_word, chosen_word)

    assert result == output
