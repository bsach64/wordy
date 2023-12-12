from os import name
import multiprocessing
from numpy import average
from wordle import check_word, print_word, EXACT
from solver import possible_matches, calculate_entropy
from copy import deepcopy
from termcolor import cprint
from pathlib import Path
import time

file_path_answers = Path("../words/answers/nyt5.txt")

with open(file_path_answers) as file:
    answers = [word.replace('\n', '') for word in file.readlines()]

file_path_allowed = Path("../words/answers/nyt5.txt")
with open(file_path_allowed) as file:
    words = [word.replace('\n', '') for word in file.readlines()]


def next_guess(entropies):
    guess = ''
    max_entropy = -1
    for thing in entropies:
        if entropies[thing] > max_entropy:
            guess = thing
            max_entropy = entropies[thing]
    return guess


def cal(index_range, stats, times, answers, words, lock):
    for index in range(*index_range):
        start = time.time()
        choice = answers[index]
        print(f"--{index}--{choice}")
        words_copy = deepcopy(words)
        wordsize = 5
        guesses = wordsize + 1

        guess = 'tares'
        previous_guess = set()
        previous_guess.add('tares')
        for i in range(0, guesses):
            status = [0] * wordsize
            score = check_word(guess, status, choice)

            print(f"Computer Guess {i + 1} : ", end="")
            print_word(guess, status)
            if score == (EXACT * wordsize):
                with lock:
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
        stop = time.time()
        with lock:
            times.append(stop - start)


def main():
    ms = time.time()
    with multiprocessing.Manager() as manager:
        stats = manager.dict({1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0})
        times = manager.list()
        lock = manager.Lock()

        index_ranges = [(1, 250), (251, 500), (501, 750), (751, 1000)]
        processes = []

        for index_range in index_ranges:
            process = multiprocessing.Process(target=cal, args=(index_range, stats, times, answers, words, lock))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        print(average(times))
        # Average number of guesses
        num = 0
        sums = 0
        for k in stats.keys():
            sums += int(k * stats[k])
            num += int(stats[k])
        print(sums / num)
    ma = time.time()
    
    print("total time: ", ma-ms)

if __name__ == "__main__":
    main()
