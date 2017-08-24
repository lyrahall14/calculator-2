"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of two inputs."""
    return int(num1) + int(num2)


def subtract(num1, num2):
    """Return the first input subtracted from the second."""

    return int(num1) - int(num2)


def multiply(num1, num2):
    """Multiply the two inputs together."""

    return int(num1) * int(num2)


def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""

    # Need to turn at least one argument to float for division to
    # not be integer division

    return float(num1) / float(num2)


def square(num1):
    """Return the square of the input."""

    # Needs only one argument

    return int(num1) ** 2


def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return int(num1) ** 3


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return int(num1) ** int(num2)  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return int(num1) % int(num2)


def my_reduce(my_function, my_list):
    """Does the operation given by the function parameter on successive elements of the list,
    giving a single element as the end result"""

    total = my_list[0]

    for i in range(len(my_list)-1):
        total = my_function(total, my_list[i+1])

    return total
