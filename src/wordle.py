import sys
from termcolor import cprint
import random

EXACT = 2
CLOSE = 1

def main():
    if (len(sys.argv)) != 2:
        sys.exit("Usage: python wordle.py wordsize")
    else:
        try:
            wordsize = int(sys.argv[1])
        except TypeError:
            sys.exit("Wordsize should be an Integer")
        if wordsize < 5 or wordsize > 8:
            sys.exit("Error: wordsize must be either 5, 6, 7 or 8")
    
    file_path = f"/home/bhavik/wordy/words/answers/{wordsize}.txt"
    with open(file_path) as file:
        words = file.readlines()    
        words = [word.replace('\n','') for word in words]
  
    choice = random.choice(words)
    guesses = wordsize + 1
    won = False
    cprint("THIS IS WORDLE", "green")
    cprint(f"You have {wordsize} tries to guess the {wordsize}-letter word")

    for i in range(0, guesses):
        guess = get_guess(wordsize)
        status = [0] * wordsize
        score = check_word(guess, status, choice)
        print(f"Guess {i + 1}:", end="")
        print_word(guess, status)
        if score == (EXACT * wordsize):
            won = True
            break
    
    if won:
        print("You won!")
    else:
        print(f"The correct word was: {choice}")


def get_guess(wordsize):
    guess = ""
    while (len(guess) != wordsize):
        guess = input(f"Input a {wordsize}-letter word: ")
    return guess

def check_word(guess, status, choice):
    score = 0
    for i, guess_letter in enumerate(guess):
        for j, choice_letter in enumerate(choice):
            if guess_letter == choice_letter:
                if i == j:
                    status[i] = EXACT
                    score += EXACT
                    break
                else:
                    status[i] = CLOSE
                    score += CLOSE
    return score

def print_word(guess, status):
    for i, letter in enumerate(guess):
        if status[i] == EXACT:
            cprint(letter, "green", end="")
        elif status[i] == CLOSE:
            cprint(letter, "yellow", end="")
        else:
            print(letter, end="")
    print()

if __name__ == "__main__":
    main()