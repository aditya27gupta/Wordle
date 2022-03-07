from unittest import mock
from src.wordle_game import WordleGame
from src.log import get_logger
from src.wordle_word_suggestor import get_input


logger = get_logger("Test input Function")
logger.disabled = True


@mock.patch("src.wordle_game.input", create=True)
def test_get_input(mocked_input):

    file_loc = "example.txt"
    tries = 6

    class_object = WordleGame(file_loc, tries, logger)

    mocked_input.side_effect = ["abcd", "xyz", "1abcd", "abcde"]

    output = class_object.get_input(1)

    assert output == "abcde"


@mock.patch("src.wordle_word_suggestor.input", create=True)
def test_suggestor_get_input(mocked_input):

    mocked_input.side_effect = [
        "abcd",
        "xyz",
        "1abcd",
        "abcde",
        "0121",
        "01234",
        "a1201",
        "01212",
    ]

    output = get_input()

    assert output == ("abcde", "01212")
