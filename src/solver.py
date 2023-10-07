import math
from itertools import product
from copy import deepcopy


def calculate_entropy(word, possible_words):
    """
    (entropy) E[information] = Summation(p(x)*information)
    This functions calculates the entropy { E[information] } for a given word.
    """
    sum = 0
    possible_status = list(product([0, 1, 2], repeat=5))
    for status in possible_status:
        probability = calculate_probability(word, list(status), possible_words)
        info = calculate_info_with_probability(probability)
        sum += (probability*info)
    return round(sum, 2)


def calculate_info_with_probability(probability):
    """
    information = -(log2(p(x))) { negative of log base 2 of probability of x }
    Calculates information { in terms of bits } for a given word.
    """
    if probability > 0:
        return -(math.log(probability, 2))
    else:
        return 0
    
def calculate_probability(guess, status, possible_words):
    """
    (probability) p = Number of words (with same status) / possible_words
    """
    return round((len(possible_matches(guess, status, possible_words))/ len(possible_words)), 4)


def possible_matches(guess, status, possible_words):
    possible_words_copy = deepcopy(possible_words)
    for i, letter in enumerate(guess):
        if status[i] == 0:
            possible_words_copy = words_without_letter(letter, possible_words_copy)
        elif status[i] == 1:
            possible_words_copy = words_containing_letter(letter, possible_words_copy, i)
        elif status[i] == 2:
            possible_words_copy = words_with_letter_at_correct_position(letter, i, possible_words_copy) 
    return possible_words_copy


def words_without_letter(letter, possible_words):
    for word in possible_words.copy():
        if letter in word:
            possible_words.remove(word)
    return possible_words


def words_containing_letter(letter, possible_words, position):
    new_possible_words = []
    for word in possible_words:
        valid = False
        for i, word_letter in enumerate(word):
            if word_letter == letter and i != position:
                valid = True
            elif word_letter == letter and i == position:
                valid = False
                break
        if valid:
            new_possible_words.append(word)
    return new_possible_words


def words_with_letter_at_correct_position(letter, position, possible_words):
    for word in possible_words.copy():
        if word[position] != letter:
            possible_words.remove(word)
    return possible_words