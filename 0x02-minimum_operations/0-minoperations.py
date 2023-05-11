#!/usr/bin/python3

"""

This module implements the minOperations function to calculate

the fewest number of operations needed to result in exactly n H

characters in a file.

"""

def minOperations(n):

    """

    Calculates the fewest number of operations needed to result in

    exactly n H characters in a file.

    Args:

        n (int): The number of H characters to achieve.

    Returns:

        int: The fewest number of operations needed to achieve n H characters.

    """

    if n <= 1:

        return 0

    # find the largest factor of n

    for i in range(n // 2, 0, -1):

        if n % i == 0:

            # recursively calculate the number of operations needed for i H characters

            return minOperations(i) + (n // i)

    # if no factor of n is found, return 0 (impossible to achieve)

    return 0
