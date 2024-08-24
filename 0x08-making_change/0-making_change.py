#!/usr/bin/python3
"""
A function to determine the fewest number of coins needed to meet a given
amount.
"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet the total amount.

    Args:
        coins (list): A list of integers representing the available coin
        denominations.
        total (int): The total amount of money that needs to be made.

    Returns:
        int: The fewest number of coins needed to make the total.
             - Returns 0 if the total is 0 or less.
             - Returns -1 if it is not possible to make the total with the
             given coins.

    Example:
        >>> makeChange([1, 2, 25], 37)
        7

        >>> makeChange([1256, 54, 48, 16, 102], 1453)
        -1
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
