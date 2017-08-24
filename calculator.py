"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

while True:
    input_string = raw_input(">")
    tokens = input_string.split(" ")

    if tokens[0] == "q":
        print "Now exiting program."
        break

    if tokens[0] == "+":
        if len(tokens) == 3:
            print add(int(tokens[1]), int(tokens[2]))
        else:
            print "I'm sorry, you entered the wrong number of numbers. Please try again."

    elif tokens[0] == "-":
        if len(tokens) == 3:
            print subtract(int(tokens[1]), int(tokens[2]))
        else:
            print "I'm sorry, you entered the wrong number of numbers. Please try again."

    elif tokens[0] == "*":
        if len(tokens) == 3:
            print multiply(int(tokens[1]), int(tokens[2]))
        else:
            print "I'm sorry, you entered the wrong number of numbers. Please try again."

    elif tokens[0] == "/":
        if len(tokens) == 3:
            print divide(int(tokens[1]), int(tokens[2]))
        else:
            print "I'm sorry, you entered the wrong number of numbers. Please try again."

    elif tokens[0] == "square":
        if len(tokens) == 2:
            print square(int(tokens[1]))
        else:
            print "I'm sorry, you entered the wrong number of numbers. Please try again."

    elif tokens[0] == "cube":
        if len(tokens) == 2:
            print cube(int(tokens[1]))
        else:
            print "I'm sorry, you entered the wrong number of numbers. Please try again."

    elif tokens[0] == "pow":
        if len(tokens) == 3:
            print power(int(tokens[1]), int(tokens[2]))
        else:
            print "I'm sorry, you entered the wrong number of numbers. Please try again."

    elif tokens[0] == "mod":
        if len(tokens) == 3:
            print mod(int(tokens[1]), int(tokens[2]))
        else:
            print "I'm sorry, you entered the wrong number of numbers. Please try again."

    else:
        print "That is not a symbol I recognize. Please try again!"
