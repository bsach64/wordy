import math

def calculate_entropy(word, status, possible_words):
    """
    (entropy) E[information] = Summation(p(x)*information)
    This functions calculates the entropy { E[information] } for a given word.
    """
    ...


def calculate_info(word, status, possible_words):
    """
    information = -(log2(p(x))) { negative of log base 2 of probability of x }
    Calculates information { in terms of bits } for a given word.
    """
    return -(math.log(calculate_probability(word, status, possible_words), 2))


def calculate_probability(guess, status, possible_words):
    """
    (probability) p = Number of words (with same status) / possible_words
    """
    return (len(possible_matches(guess, status, possible_words)) / len(possible_words))


def possible_matches(guess, status, possible_words):
    for i, letter in enumerate(guess):
        if status[i] == 0:
            possible_words = words_without_letter(letter, possible_words)
        elif status[i] == 1:
            possible_words = words_containing_letter(letter, possible_words)
        elif status[i] == 2:
            possible_words = words_with_letter_at_correct_position(letter, i, possible_words) 
    return possible_words

def words_without_letter(letter, possible_words):
    for word in possible_words.copy():
        if letter in word:
            possible_words.remove(word)
    return possible_words


def words_containing_letter(letter, possible_words):
    for word in possible_words.copy():
        if letter not in word:
            possible_words.remove(word)
    return possible_words


def words_with_letter_at_correct_position(letter, position, possible_words):
    for word in possible_words.copy():
        if word[position] != letter:
            possible_words.remove(word)
    return possible_words