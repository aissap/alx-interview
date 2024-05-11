#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """
    Calculate the minimum number of operations needed to achieve 'n' characters
    in a text file using only 'Copy All' and 'Paste' operations.

    Args:
        n  : The target number of characters

    Returns:
        int: The minimum number of operations required
    """
    if n <= 1:
        return 0

    operations = 0
    H = 2
    while n > 1:
        while n % H == 0:
            operations += H
            n //= H
        H += 1

    return operations
