import argparse
from wordle import play


parser = argparse.ArgumentParser(
    description="Play and Solve wordle games"
)
group = parser.add_mutually_exclusive_group()

# Play
group.add_argument(
    "-p",
    "--play",
    help="Play wordle with p letters",
    default=5,
    type=int,
    choices=[4, 5, 6, 7]
)

# Compete
group.add_argument(
    "-c",
    "--compete",
    help="Compete against the solver in a game of c letters",
    default=5,
    type=int,
    choices=[4, 5, 6, 7]
)

args = parser.parse_args()

if args.play:
    play(args.play)
elif args.compete:
    ...
