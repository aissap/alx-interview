#!/usr/bin/python3
""" N Queens Problem """
import sys


def validate_input():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(sys.argv[1])

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def queens(n, row=0, columns=[], diagonals1=[], diagonals2=[]):
    """ Generate all valid positions for N Queens problem """
    if row == n:
        yield columns
    else:
        for col in range(n):
            if col not in columns and
            row + col not in diagonals1 and
            row - col not in diagonals2:
                yield from queens(
                        n, row + 1,
                        columns + [col],
                        diagonals1 + [row + col],
                        diagonals2 + [row - col]
                )


def solve_nqueens(n):
    """ Solve N Queens problem and print each solution """
    for solution in queens(n):
        print([[i, solution[i]] for i in range(n)])


def main():
    n = validate_input()
    solve_nqueens(n)


main()
