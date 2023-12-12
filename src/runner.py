import argparse
from wordle import play
from solver import best_first_guess
from user_v_comp import compete
from test_solver_multiprocessing import simulate

parser = argparse.ArgumentParser(
    description="Play and Solve wordle games"
)
group = parser.add_mutually_exclusive_group()

# Play
group.add_argument(
    "-p",
    "--play",
    help="Play wordle with p letters",
    type=int,
    choices=[5, 6, 7]
)

# Compete
group.add_argument(
    "-c",
    "--compete",
    help="Compete against the solver in a game of c letters",
    type=int,
    choices=[5, 6, 7]
)

# Best First Guess
group.add_argument(
    "-f",
    "--first",
    help="Best first guesses & their entropies",
    type=int,
    choices=[5, 6, 7]
)

# Stats
group.add_argument(
    "-s",
    "--stats",
    help="Stats related to the solver",
    type=int,
    choices=[5, 6, 7]
)

# Simulate
group.add_argument(
    "-r",
    "--run",
    help="Runs the solver on a 100 random words",
    type=int,
    choices=[5, 6, 7]
)
args = parser.parse_args()

if args.play:
    play(args.play)
elif args.first:
    word, entropy = best_first_guess(args.first)
    print(f"Best Possible word: {word}")
    print(f"Entropy: {entropy}")
elif args.compete:
    compete(args.compete)
elif args.stats:
    if args.stats == 6:
        print("Average Time Taken: 0.256")
        print("Average Number of Guesses: 2.811")
    elif args.stats == 5:
        print("Average Time Taken: 1.079")
        print("Average Number of Guesses: 3.565")
    elif args.stats == 7:
        print("Average Time Taken: 0.181")
        print("Average Number of Guesses: 2.728")
elif args.run:
    simulate(args.run)
