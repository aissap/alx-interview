#!/usr/bin/python3
"""
Prime Game module
"""


def sieve_of_eratosthenes(n):
    """Generate a list of prime numbers up to n"""
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes


def count_prime_moves(n, primes):
    """The number of for a given n"""
    available = [True] * (n + 1)
    moves = 0

    for prime in primes:
        if prime > n:
            break
        if available[prime]:
            moves += 1
            for multiple in range(prime, n + 1, prime):
                available[multiple] = False

    return moves


def isWinner(x, nums):
    """Determine the winner of the prime game"""
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        moves = count_prime_moves(n, primes)
        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None