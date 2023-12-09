import json
from wordle import check_word, print_word, EXACT
from solver import possible_matches, calculate_entropy
from copy import deepcopy

file_path_answers = "/home/bhavik/Code/wordy/words/allowed/allowed_5_letter.txt"
with open(file_path_answers) as file:
    answers = file.readlines()
    answers = [word.replace('\n', '') for word in answers]


file_path_allowed = "/home/bhavik/Code/wordy/words/allowed/allowed_5_letter.txt"
with open(file_path_answers) as file:
    words = file.readlines()
    words = [word.replace('\n', '') for word in words]


things = dict()
with open('entropies4.json') as file:
    things = json.load(file)


def next_guess(entropies):
    guess = ''
    max_entropy = -1
    for thing in entropies:
        if entropies[thing] > max_entropy:
            guess = thing
            max_entropy = entropies[thing]
    return guess


print(next_guess(things))


def main():
    stats = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    help = []
    for choice in answers:
        words_copy = deepcopy(words)
        wordsize = 5
        guesses = wordsize + 1
        print(choice)
        guess = 'tares'
        previous_guess = set()
        previous_guess.add('tares')
        for i in range(0, guesses):
            status = [0] * wordsize
            score = check_word(guess, status, choice)
            print(f"Guess {i + 1} : ", end="")
            print_word(guess, status)
            if score == (EXACT * wordsize):
                stats[i + 1] += 1
                print(stats)
                break
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

    print(stats)
    print(help)


if __name__ == "__main__":
    main()
