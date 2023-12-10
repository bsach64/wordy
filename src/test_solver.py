
import sys
import random
import json
from wordle import check_word, print_word, EXACT, get_guess
from solver import possible_matches, calculate_entropy
from copy import deepcopy
from termcolor import cprint


file_path_answers = "/home/scifre/Desktop/wordy/words/answers/5.txt"

with open(file_path_answers) as file:
    answers = file.readlines()
    answers = [word.replace('\n', '') for word in answers]


file_path_allowed = "/home/scifre/Desktop/wordy/words/allowed/allowed_5_letter.txt"
with open(file_path_allowed) as file:
    words = file.readlines()
    words = [word.replace('\n', '') for word in words]


def next_guess(entropies):
    guess = ''
    max_entropy = -1
    for thing in entropies:
        if entropies[thing] > max_entropy:
            guess = thing
            max_entropy = entropies[thing]
    return guess


def main():
    stats = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, "nope": 0}
    help = []
    choice = random.choice(answers)
    print(f"----{choice}")
    words_copy = deepcopy(words)
    wordsize = 5
    guesses = wordsize + 1
    won = False
    comp_won = False
    cprint(f"{wordsize} letter - WORDLE", "green")
    cprint(f"You have {guesses} tries to guess the {wordsize}-letter word\n\n")

    #print(choice)
    guess = 'tares'
    previous_guess = set()
    previous_guess.add('tares')
    for i in range(0, guesses):
        user_guess = get_guess(words)
        user_status = [0]*wordsize
        user_score = check_word(user_guess, user_status, choice)
        status = [0] * wordsize
        score = check_word(guess, status, choice)
                
        print('\033[F', '\033[K' f"\rUser Guess {i + 1} : ", end='')
        print_word(user_guess, user_status)
        if user_score == (EXACT * wordsize):
            won = True
            break
        
        print(f"Computer Guess {i + 1} : ", end="")
        print_word(guess, status)
        if score == (EXACT * wordsize):
            comp_won = True
            stats[i + 1] += 1
            print(stats)
            break
        print()
        words_copy = possible_matches(guess, status, words_copy, previous_guess)
        entropies = dict()
        for word in words_copy:
            entropies[word] = calculate_entropy(word, words_copy)
        guess = next_guess(entropies)
        previous_guess.add(guess)
        if i == 5:
            stats[7] += 1
            help.append(choice)
            print(help)

    if won:
        print("\nCongratulation!, You Won")
    elif comp_won:
        print("\nComputer Won, better luck next time!")
    else:
        print("\nSorry, Both failed")
        
    #print(stats)
    
    #print(help)


if __name__ == "__main__":
    main()
