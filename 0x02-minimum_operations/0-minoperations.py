#!/usr/bin/python3
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
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
