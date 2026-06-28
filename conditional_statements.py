"""
Conditional Statements:
Is like a checkpoint that checks a condition
    - If true then run some block of code
    - If false then skip it
"""
# score = int(input(": "))

# ? Standalone if:
# if score >= 90:
#     # Nested if's
#     project = input("Y/N: ").lower()
#     if project.startswith('y'):
#         print("A+")
#     else:
#         print("A")
# ? Multiple conditions:
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# ? Two way decision:
# else:
#     print("F")

# ? Independent ifs:
# score = int(input("Score: "))
# project = input("y/n: ").lower()

# if score >= 90:
#     print("High Score")
# else:
#     print("Low Score")

# if project.startswith("y"):
#     print("Project submitted")

# else:
#     print("Project not submitted")

# ? Inline statements or ternary operator: only to check simple logic

# score = 95

# grade = ("A" if score >= 90 else "B" if score >= 80 else "F")
# print(grade)

# ? Case match: Evaluate a value against multiple values, run the code of the first match

# TODO: Convert the full name of countries into 2 letter aberration
country = "India"

match country:
    case "United States" | "USA":
        print("US")
    case "India" | "IND":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _:
        print("Unknown Country!")
