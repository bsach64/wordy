# wordy
## How to Run the Project Locally
1. Clone the Repository
`git clone https://github.com/bsach64/wordy`
2. `cd wordy/src`
3. Run `python runner.py --help`
```
usage: runner.py [-h] [-p {5,6,7} | -c {5,6,7} | -f {5,6,7} | -s {5,6,7} | -r {5,6,7} | -g GUESS]

Play and Solve wordle games

options:
  -h, --help            show this help message and exit
  -p {5,6,7}, --play {5,6,7}
                        Play wordle with p letters
  -c {5,6,7}, --compete {5,6,7}
                        Compete against the solver in a game of c letters
  -f {5,6,7}, --first {5,6,7}
                        Best first guesses & their entropies
  -s {5,6,7}, --stats {5,6,7}
                        Stats related to the solver
  -r {5,6,7}, --run {5,6,7}
                        Runs the solver on a 100 random words
  -g GUESS, --guess GUESS
                        Give a 5, 6, 7 letter word to guess
```
