"""Math functions for calculator."""
from functools import reduce

def add(num_list):
    """Return the sum of a list of integers."""
    total = 0

    for item in num_list:
        total += int(item)

    return total


def subtract(num_list):
    """Takes in a list and returns the result of each number subtracted from its previous neighbor."""
    total = 0

    for item in num_list:
        total -= int(item)

    return total


def multiply(num_list):
    """Takes in a list and returns the multiplication of all its elements."""
    total = num_list[0]

    for item in num_list[1:]:
        total *= int(item)

    return total


def divide(num_list):
    """Takes in a list and returns the division of each number by its previous neighbor"""

    # Need to turn at least one argument to float for division to
    # not be integer division
    total = num_list[0]

    for item in num_list[1:]:
        total /= float(item)

    return total


def square(num_list):
    """Return a new list with each number in the original list squared."""
    new_list = []

    for item in num_list:
        new_list.append(item*item)

    return new_list


def cube(num_list):
    """Return a new list with each number in the original list cubed."""
    new_list = []

    for item in num_list:
        new_list.append(item*item*item)

    return new_list


def power(num_list):
    """Return a new list with each number raised to the power of the first element."""
    new_list = []

    for item in num_list:
        new_list.append(item ** num_list[0])

    return new_list


def mod(num_list):
    """Return a new list with each number modulo'd by the first element."""
    new_list = []

    for item in num_list:
        new_list.append(item % num_list[0])

    return new_list
