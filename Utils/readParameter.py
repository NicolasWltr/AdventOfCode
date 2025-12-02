import argparse

def read_parameter():
    parser = argparse.ArgumentParser()

    parser.add_argument('--year', type=int, required=True, help='Year of the Advent of Code challenge')
    parser.add_argument('--day', type=int, required=True, help='Day of the Advent of Code challenge')
    parser.add_argument('--submit', action='store_true', default=False, help='Submit answer to AoC')

    args = parser.parse_args()

    return args.year, args.day, args.submit