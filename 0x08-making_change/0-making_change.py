#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total
    """
    
    if total <= 0:

        return 0

    dp = [0] + [float("inf")] * total

    coin_set = set(coins)

    for i in range(1, total + 1):

        for coin in sorted(coin_set):

            if i >= coin:

                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float("inf") else -1
