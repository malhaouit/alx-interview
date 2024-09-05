#!/usr/bin/python3
"""Prime Game"""


def sieve_of_eratosthenes(n):
    """Use Sieve of Eratosthenes to generate a list of primes up to n."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False

    return is_prime


def prime_game_outcomes(max_n):
    """
    Precompute the outcome of the game for all n from 1 to max_n.
    Returns a list where result[i] is True if Maria wins when
    playing with 1..i, and False if Ben wins.
    """
    # Precompute primes up to max_n using Sieve of Eratosthenes
    is_prime = sieve_of_eratosthenes(max_n)

    # outcomes[i] is True if Maria wins the game with n = i, False if Ben wins
    outcomes = [False] * (max_n + 1)  # Ben wins if no primes available

    for n in range(2, max_n + 1):
        # Set of remaining numbers in this round
        primes_left = [i for i in range(2, n + 1) if is_prime[i]]

        # Current player: True for Maria, False for Ben
        maria_turn = True

        while primes_left:
            # Remove the first prime and its multiples
            p = primes_left[0]
            primes_left = [x for x in primes_left if x % p != 0]

            # Switch turn
            maria_turn = not maria_turn

        # If maria_turn is False, Maria lost, otherwise Maria won
        outcomes[n] = not maria_turn

    return outcomes


def isWinner(x, nums):
    """
    Determines the winner of x rounds of the game.

    Arguments:
    x -- the number of rounds
    nums -- an array of integers representing the upper bound n for each round

    Returns:
    The name of the player who won the most rounds, or None if it is a tie.
    """
    if x == 0 or not nums:
        return None

    # Precompute the game outcomes for all possible values of n in nums
    max_n = max(nums)
    outcomes = prime_game_outcomes(max_n)

    # Count wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if outcomes[n]:  # Maria wins this round
            maria_wins += 1
        else:  # Ben wins this round
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
