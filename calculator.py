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
        tokens.remove("+")
        if len(tokens) >= 2:
            print my_reduce(add, tokens)
        else:
            print "I'm sorry, you entered too few numbers. Please try again."

    elif tokens[0] == "-":
        tokens.remove("-")
        if len(tokens) >= 2:
            print my_reduce(subtract, tokens)
        else:
            print "I'm sorry, you entered too few numbers. Please try again."

    elif tokens[0] == "*":
        tokens.remove("*")
        if len(tokens) >= 2:
            print my_reduce(multiply, tokens)
        else:
            print "I'm sorry, you entered too few numbers. Please try again."

    elif tokens[0] == "/":
        tokens.remove("/")
        if len(tokens) >= 2:
            print my_reduce(divide, tokens)
        else:
            print "I'm sorry, you entered too few numbers. Please try again."

    elif tokens[0] == "square":
        tokens.remove("square")
        if len(tokens) >= 1:
            print my_reduce(square, tokens)
        else:
            print "I'm sorry, you entered too few numbers. Please try again."

    elif tokens[0] == "cube":
        tokens.remove("cube")
        if len(tokens) >= 1:
            print my_reduce(cube, tokens)
        else:
            print "I'm sorry, you entered too few numbers. Please try again."

    elif tokens[0] == "pow":
        tokens.remove("pow")
        if len(tokens) >= 2:
            print my_reduce(power, tokens)
        else:
            print "I'm sorry, you entered too few numbers. Please try again."

    elif tokens[0] == "mod":
        tokens.remove("mod")
        if len(tokens) >= 2:
            print my_reduce(mod, tokens)
        else:
            print "I'm sorry, you entered too few numbers. Please try again."

    else:
        print "That is not a symbol I recognize. Please try again!"
