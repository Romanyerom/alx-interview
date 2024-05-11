#!/usr/bin/python3
"""
This module defines a function minOperations that calculates the
minimum number of operations needed to reach exactly n 'H' characters
using "Copy All" and "Paste" operations.
"""

def minOperations(n):
    if n <= 1:
        return 0
    
    ops = 0
    factor = 2
    
    # Process each factor
    while factor * factor <= n:
        while n % factor == 0:
            ops += factor
            n //= factor
        factor += 1

    # If n is a prime number greater than 1
    if n > 1:
        ops += n

    return ops

if __name__ == "__main__":
    # Examples to test the function
    print("Min # of operations to reach 4 chars:", minOperations(4))  # Output: 4
    print("Min # of operations to reach 12 chars:", minOperations(12))  # Output: 7
