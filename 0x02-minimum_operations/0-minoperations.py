#!/usr/bin/python3
"""
This module provides a function to calculate the minimum number of operations
required to achieve exactly `n` 'H' characters in a text file using only
two operations: "Copy All" and "Paste".
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to achieve exactly n 'H'
    characters in the file.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required to achieve n 'H'
        characters. If n is impossible to achieve, returns 0.
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
