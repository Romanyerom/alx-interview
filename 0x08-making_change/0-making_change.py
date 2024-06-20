#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
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

# Testing the function
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

