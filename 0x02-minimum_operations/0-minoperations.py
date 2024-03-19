#!/usr/bin/python3
"""Min operation to print n of H"""


def minOperations(n):
    """Min Operation"""
    total_operations = 0
    current_factor = 2

    while n > 1:
        while n % current_factor == 0:
            total_operations += current_factor
            n /= current_factor
        current_factor += 1

    return total_operations
