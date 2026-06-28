"""
? Loops:
Is a control flow that repeats a block of code again and again till a condition is met

"""
"""
? For loop: 
Go thru a group of items one by one to do something for each item
- for
- loop variable : (i)
- operator : in 
- (1,2,3) : Sequence

for i in (1,2,3):
    print(i)

? Python Iterator:
An object that lets you go thru items one by one in a sequence.

? Range:
will help to iterator to iterate form start value to end value
- (Start,)
- (Start,end+1)
- (Start, end+1, step)
"""
print("=" * 45)

# With Sequence:
items = (1, 2, 3, 4, 5)

for i in items:
    print(f"Round: {i}")

print("=" * 45)

# With list:
files = ["Report.csv", "Budget.csv", "P&L.csv", "Breakeven_report.csv"]

for i in files:
    print(f"Files - {i}")

print("=" * 45)

# With string:
str = "sayandip loves puchu"

for i in str:
    print(f"char: {i}")

print("=" * 45)

# printing 2's table: using range
print(f"==== 2's table ====")

for i in range(1, 11):
    print(f"2 x {i} = {i*2}")

print("=" * 45)

# printing even numbers:
print(f"==== even numbers upto 20 ====")

for i in range(0, 21, 2):
    print(f"is even: {i}")

print("=" * 45)

# printing odd numbers:
print(f"==== odd numbers upto 20 ====")

for i in range(1, 21, 2):
    print(f"is odd: {i}")

print("=" * 45)

# Summation:
print(f"==== Summation ====")
score = [80, 25, 60, 45, 69, 45]
total = 0

for i in score:
    total += i
    print(f"Current Total: {total}")

print(f"Final Total: {total}")

print("=" * 45)

# Data Cleaning with loops:
print(f"==== Data Cleaning ====")
"""
TODO's: 
- Remove spaces
- All file first letter should be capital only
- All extension should be csv
"""
files = [
    " Report.csv  ",
    "BUDGET.csv",
    "P&L.csv  ",
    "    breakeven_report.txt"
]

for file in files:
    file = file.strip().capitalize().replace("txt", "csv")
    print(f"Processing {file} ✅")

print("=" * 45)
