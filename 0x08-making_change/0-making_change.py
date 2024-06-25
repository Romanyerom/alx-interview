#!/usr/bin/python3

"""
This module provides a function to determine the minimum number of coins needed
to meet a given amount total using a dynamic programming approach.
If the total cannot be met by any combination of the coins, the function returns -1.
"""

def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to meet a given amount total.
    If the total cannot be met by any combination of the coins, return -1.
    
    Args:
    coins (list): A list of the values of the coins in your possession.
    total (int): The total amount to be met with the coins.
    
    Returns:
    int: The fewest number of coins needed to meet total, or -1 if total cannot be met.
    """
    if total < 0:
        return -1
    if total == 0:
        return 0

    # Initialize DP array with infinity, and dp[0] with 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Loop through each coin
    for coin in coins:
        # Update the dp array for each amount that can be reached by the current coin
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Check if we have found a solution or not
    return dp[total] if dp[total] != float('inf') else -1

# Testing the function with various cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 25], 37, 7),
        ([1256, 54, 48, 16, 102], 1453, -1),
        ([2, 5, 10, 1], 27, 4),  # Example case: 10+10+5+2
        ([1, 3, 4], 6, 2),       # Example case: 3+3
        ([2], 3, -1),            # Impossible case
        ([1], 0, 0),             # Zero total
        ([5, 3, 1], 7, 2),       # 3+4 or 5+2
        ([1, 2, 5], -5, -1),     # Negative total
    ]

    for coins, total, expected in test_cases:
        result = makeChange(coins, total)
        print(f"makeChange({coins}, {total}) = {result} (Expected: {expected})")

