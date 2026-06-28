"""
TODO: Generate a random integer between 1 to 100, and check the result is even or odd number 

"""

import random

rand = random.randint(1, 100)

if rand % 2 == 0:
    print(f"{rand} is even")
else:
    print(f"{rand} is odd")
