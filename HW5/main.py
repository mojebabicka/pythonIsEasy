#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Print out numbers from 1 to 100.
With the increasing priority:
- If the number is divisible by 3 print Fizz instead.
- If it is divisible by 5 print Buzz.
- If it is divisible by both print FizzBuzz.
- If it is prime print Prime.

For the purposes of the Pirple Python is easy course.
Formatted according to PEP8.
"""

# Create list of numbers for testing of primes
test_numbers = []
for i in range(2, 101):
    test_numbers.append(i)

"""One is a very special number so we print it out of the loop.
It does not fall in any category but it complicates testing
for primes, so we take it out of the loop.
"""
print(1)

# All other numbers are checked within the loop
for i in range(2, 101):
    # Prime test (not nice, not efficient, but correct)
    prime_test = True
    temp_test_numbers = test_numbers.copy()
    temp_test_numbers.remove(i)
    for j in temp_test_numbers:
        if i % j == 0:
            prime_test = False
            break
    # Check numbers and print appropriate message
    if prime_test:
        print("Prime")
    elif i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
