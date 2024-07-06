#!/usr/bin/python3

def isWinner(x, nums):
    if not nums or x < 1:
        return None

    max_n = max(nums)

    # Sieve of Eratosthenes to find all primes <= max_n
    is_prime = [True] * (max_n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False
    primes = [num for num, prime in enumerate(is_prime) if prime]

    # Dynamic programming array to store win/lose for each number
    dp = [0] * (max_n + 1)  # dp[i] will be 1 if starting with i is a winning state for Maria

    # Precompute the winner for every number from 0 to max_n
    for i in range(2, max_n + 1):
        for prime in primes:
            if prime > i:
                break
            if dp[i - prime] == 0:
                dp[i] = 1
                break

    # Determine the winner for each game in nums
    ben_wins, maria_wins = 0, 0
    for n in nums:
        if dp[n] == 1:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None

if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))


