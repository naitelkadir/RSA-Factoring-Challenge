#!/usr/bin/python3
import sys


def factorize(number):
    factors = []
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            factors.append((i, number // i))
            return factors


def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    input_file = sys.argv[1]
    try:
        with open(input_file, 'r') as file:
            for line in file:
                number = int(line.strip())
                factor_pairs = factorize(number)
                for p, q in factor_pairs:
                    print(f"{number}={p}*{q}")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")


if __name__ == '__main__':
    main()

