import argparse
from core.cube import Cube
from core.kociemba import KociembaSolver

parser = argparse.ArgumentParser()
parser.add_argument("--scramble", type=str, required=True)
args = parser.parse_args()

solution = KociembaSolver().solve(Cube().scramble(args.scramble))
print(" ".join(solution))
