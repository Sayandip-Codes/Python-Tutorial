# x  = "6"
# y = 9

# print(x + y)  = this will throw an error because python can't concatinate

# print(y + x) : TypeError: unsupported operand type(s) for +: 'int' and 'str'

# # Data types:
# a = 10  # int
# b = 21.05  # float
# c = "Heya!"  # String
# d = '1236'  # String
# f = False  # bool : it is case sensitive
# e = True  # bool : it is case sensitive
# h = None #unknown data type
# i = "" #blank string
# g = "  " #string =  empty space

text = "hi"
num = 1000

print(len(text))  # Returns length of a string

print(text.upper())  # Will turn into a uppercase
print(num.bit_length())  # Number of bits necessary to represent self in binary


# TypeCasting in python:
digit = 145556
print("OTP: ", type(str(digit)))

otp = "456356"
print("OTP: ", type(int(otp)))
