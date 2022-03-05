import pytest

from src.wordle_word_suggestor import wordle_word_check


input_output = [
    ("abcde", "00000", "ajdhe", False),
    ("abcde", "22222", "ajdhe", False),
    ("abcde", "22222", "abcde", True),
    ("abcde", "11111", "edbca", True),
    ("crane", "01201", "above", False),
    ("syste", "12012", "tyise", True),
]


@pytest.mark.parametrize(
    "input_word, comp_matrix, wordle_list_word, output", input_output
)
def test_compare_test(input_word, comp_matrix, wordle_list_word, output):

    result = wordle_word_check(input_word, comp_matrix, wordle_list_word)

    assert result == output
