#!/usr/bin/env python3

"""
Programming:
Listing all things that must happen to solve a problem.
"""

"""
Ask user to input their name
then store in a variable called name
print out, "Hello" followed by their name
"""
name = input("What is your name? ")
print("Hello", name)

"""
Ask user to input two numbers and store in two variables num_one, num_two
Convert the two numbers from string to integers
Add two numbers and store the result in variable called sum
Subtract two numbers and store the result in variable called difference
Multiply two number and store the result in variable called product
Divide two numbers and store in variable called quotient
Find the remainder of these two numbers and store in variable, modulus
Print the result in format: 1 + 2 = 3
"""
num_one, num_two = input("Enter two numbers of your choice: ").split()
num_one = int(num_one)
num_two = int(num_two)
sum = num_one + num_two
difference = num_one - num_two
product = num_one * num_two
quotient = num_one / num_two
modulus = num_one % num_two
print("{} + {} = {}".format(num_one, num_two, sum))
print("{} - {} = {}".format(num_one, num_two, difference))
print("{} * {} = {}".format(num_one, num_two, product))
print("{} / {} = {}".format(num_one, num_two, quotient))
print("{} % {} = {}".format(num_one, num_two, modulus))

"""
Problem:
    Ask user to input miles and convert to Kilometers
    Kilometers = miles * 1.60934
    Print in format:
        4 miles equals 7.01 Kilometers
"""
miles = input("Enter miles: ")
miles = int(miles)
kilometers = (miles * 1.60934)
print("{} miles equals {} kilometers".format(miles, kilometers))

"""
Calculator:
    Ask user to input two numbers plus an operator
    And store in variables num_one, num_two, and operator
    If operator is +, -, *, /, % perform claculations based on that
    Print the result in format:
        1 + 2 = 3
"""
num_one, num_two, operator = input("Enter calculation: ").split()
if operator == "+":
    sum = num_one + num_two
    print("{} + {} = {}".format(num_one, num_two, sum))
elif operator == "-":
    sub = num_one - num_two
    print("{} - {} = {}".format(num_one, num_two, sub))
else:
    print("Syntax Error!")
