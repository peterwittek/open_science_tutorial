# The header is missing and there are unnecessary imports
import random #getopt, sys, os

# This line will only work in Python 2
print("This script is not perfect")

# The following loop could be written in a single line with list comprehension
random_numbers = [random.random() for i in range(10)]

# Don't do this. Just don't.
for i in range(len(random_numbers)):
    print random_numbers[i]

# This loop could be rewritten with enumerate
i = 0
for r in random_numbers:
    print(i, r)
    i += 1

# This is not C
if(len(random_numbers)>5): print("Lots of random numbers here")
