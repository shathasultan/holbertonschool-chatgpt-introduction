#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Parameters:
    n (int): The number for which to calculate the factorial. Must be a non-negative integer.

    Returns:
    int: The factorial of the number n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the number from command line arguments and calculate factorial
f = factorial(int(sys.argv[1]))
print(f)

