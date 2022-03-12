# Wordle


![Pytest](https://github.com/aditya27gupta/Wordle/actions/workflows/python-test.yml/badge.svg)
![CodeQL](https://github.com/aditya27gupta/Wordle/actions/workflows/codeql-analysis.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![coverage-report](./assets/coverage_image.png?raw=true "Coverage Report")
![GitHub repo size](https://img.shields.io/github/repo-size/aditya27gupta/WORDLE)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

Players have six attempts to guess a five-letter word, with feedback given for each guess in the form of colored tiles indicating when letters match or occupy the correct position.

Example:

Wordle Word: **S T R A P S**

Input: **S L E E P**

Here,

S would be shown colored Green implying it is present and in right position

L would be normal as it is not present in Wordle Word

P would be colored Yellow implying it is present in word just in wrong position


#### Run Wordle Game
```python
python3 src/main.py
```


## How to use Wordle Word Suggestor

Compare matrix is defined with numbers ranging from 0 to 2.
- When the letter is colored green, compare matrix value is 2
- When the letter is colored yellow, compare matrix value is 1
- When the letter is not colored, compare matrix value is 0


Example:

Wordle Word: **S T R A P S**

Input: **S L E E P**

Here S will be colored green, L E E will not be colored differently and P will be colored yellow.

So, compare matrix will be: **20001**


#### Run Wordle Word Suggestor
```python
python3 src/wordle_word_suggestor.py
```
