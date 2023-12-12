from os import name
import sys
from numpy import average
from wordle import check_word, print_word, EXACT
from solver import possible_matches, calculate_entropy, best_first_guess
from copy import deepcopy
from termcolor import cprint
from pathlib import Path
import time


def next_guess(entropies):
    guess = ''
    max_entropy = -1
    for thing in entropies:
        if entropies[thing] > max_entropy:
            guess = thing
            max_entropy = entropies[thing]
    return guess


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage test_solver.py wordsize")
    else:
        try:
            wordsize = int(sys.argv[1])
        except:
            sys.exit("Wordsize should be an integer!")
    file_path_answers = Path(f"../words/answers/{'nyt5' if wordsize==5 else wordsize}.txt")

    with open(file_path_answers) as file:
        answers = file.readlines()
        answers = [word.replace('\n', '').strip() for word in answers]


    file_path_allowed = Path(f"../words/answers/{'nyt5' if wordsize==5 else wordsize}.txt")
    with open(file_path_allowed) as file:
        words = file.readlines()
        words = [word.replace('\n', '').strip() for word in words]

    ms = time.time()
    stats = {(i):0 for i in range(1, wordsize+2)}
    help = []
    times = [] 
    for index, choice in enumerate(answers):
        
        start = time.time()
        print(f"--{index}--{choice}")
        words_copy = deepcopy(words)
        
        guesses = wordsize + 1
        
        guess, _ = best_first_guess(wordsize)
        previous_guess = set()
        previous_guess.add(guess)
        for i in range(0, guesses):

            status = [0] * wordsize
            score = check_word(guess, status, choice)

            print(f"Computer Guess {i + 1} : ", end="")
            print_word(guess, status)
            if score == (EXACT * wordsize):
                stats[i + 1] += 1
                print(stats)
                break
            print()
            words_copy = possible_matches(guess, status, words_copy, previous_guess)
            entropies = dict()
            for word in words_copy:
                entropies[word] = calculate_entropy(word, words_copy, wordsize)
            guess = next_guess(entropies)
            previous_guess.add(guess)
        stop = time.time()
        
        times.append(stop-start)
        
        if(index==1000):
            break
    print(average(times))
    #average number of guesses
    num = 0
    sums = 0
    for k in stats.keys():
        sums += int (k*stats[k])
        num += int(stats[k])
    print(sums/num)
    ma = time.time()
    print("total time: ", ma-ms)
        
            
            
        

if __name__=="__main__":
    main()
