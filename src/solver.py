import math
from itertools import product
from wordle import CLOSE, EXACT
import json


def calculate_entropy(word: str, possible_words: [str], repeat=5):
    """
    (entropy) E[information] = Summation(p(x)*information)
    This functions calculates the entropy { E[information] } for a given word.
    Rounded to two decimal places.
    """
    sum = 0
    possible_status = list(product([0, 1, 2], repeat=repeat))
    for status in possible_status:
        probability = calculate_probability(word, list(status), possible_words)
        info = calculate_info_with_probability(probability)
        sum += probability*info
    return round(sum, 2)


def calculate_info_with_probability(probability: float):
    """
    information = -(log2(p(x))) { negative of log base 2 of probability of x }
    Calculates information { in terms of bits } for a given word.
    """
    if probability > 0:
        return -(math.log(probability, 2))
    else:
        return 0


def calculate_probability(guess: str, status: [int], possible_words: [str]):
    """
    (probability) p = Number of words (with same status) / possible_words
    Rounded to 4 decimal places.
    """
    return round((len(possible_matches(guess, status, possible_words)) / len(possible_words)), 4)


def possible_matches(guess: str, status: [int], possible_words: [str], previous_guess=set()) -> [str]:
    """
    Returns a list of the next possible guess
    """
    matches = []
    for word in possible_words:
        if _is_possible_match(guess, status, word) and word not in previous_guess:
            matches.append(word)
    return matches


def _is_possible_match(guess: str, status: [int], match: str):
    """
    Given a guess & its status, returns a bool whether match can be the next guess.
    """
    nope = set()  # Match should not contain these letters
    not_contains = dict()  # key: position where value: letter should not be
    exact = set()

    for i, letter in enumerate(guess):
        if status[i] == EXACT:
            if letter != match[i]:
                return False
            else:
                exact.add((i, letter))
        elif status[i] == 0:
            nope.add(letter)
        if status[i] == CLOSE:
            not_contains[i] = letter

    for letter in not_contains.values():
        if letter in nope:
            nope.remove(letter)

    for letter in not_contains.values():
        if letter not in match:
            return False

    for i, letter in enumerate(match):
        if (i, letter) in exact:
            continue
        if letter in nope:
            return False
        if i in not_contains:
            if not_contains[i] == letter:
                return False

    if len(guess) != len(set(guess)):
        count_close = _count_close_occurences(guess, status)
        count_match = _count_close_occurences(match, status)
        for letter in count_close:
            if letter in count_match:
                if count_match[letter] < count_close[letter]:
                    return False
            else:
                return False
    return True


def _count_close_occurences(guess, status):
    counts = dict()
    for i, letter in enumerate(guess):
        if status[i] == CLOSE:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
    return counts


def best_first_guess(wordsize: int):
    entropies = dict()
    with open(f'entropies{wordsize}.json') as file:
        entropies = json.load(file)

    guess = ''
    max_entropy = -1
    for thing in entropies:
        if entropies[thing] > max_entropy:
            guess = thing
            max_entropy = entropies[thing]
    return guess, max_entropy
