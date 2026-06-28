# Numeric:
import math
import random

# Types and Conversation:
x = 5
y = 6.23
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))

u = "25"
print(type(u))
u = int(u)
print(type(u))

pi = "3.14"
pi = float(pi)
print(pi)

print("=" * 45)

# Math operators:
print("Addition: ", 5 + 6)  # Addition
print("Subtraction:  ", 8 - 5)  # Subtraction
print("Multiplication: ", 5 * 6)  # Multiplication
print("Division: ", 13 / 6)  # Division
print("Floor value: ", 13 // 6)  # Floor value
print("Modular Division: ", 31 % 6)  # Modular Division
print("Times: ", 5 ** 3)  # Multiplication

print("=" * 45)

# Rounding function:

# TODO:
# Measure distance point a to b
print(f"Absolute Value: {abs(2 - 10)}")

# TODO:
# Rounding Numbers:
price = 12.56356942
print(f"Ceil: {math.ceil(price)}")
print(f"Floor: {math.floor(price)}")
print(f"Round: {round(price)}")
print(f"Round-decimal: {round(price, 2)}")
print(f"Trunc: {math.trunc(price)}")

print("=" * 45)

# Rounding function:
print(f"Random num: {random.random()}")
print(f"Random int: {random.randint(1, 6)}")

# TODO: Create a 4 digit OTP generator:
otp = random.randint(1000, 9999)
print(f"OTP: {otp}")

# Validation:
x = 7.5
print(x.is_integer())

y = 64
print(isinstance(y, int))
