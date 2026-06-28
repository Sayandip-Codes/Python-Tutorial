"""
Text Formatter
Input: " Hello, WORLD!! "

TODO: Output: "hello, world!"
"""
# text = input("Enter your text here: ")
# formatted_text = text.lower().strip().replace("!!", "!")
# print(f"Clean text: {formatted_text}")


"""
Context: Practice splitting names, extracting initials, and formatting them in different styles.

Input: "Sayandip Bhattacharya"

Output: "S B"

TODO: Split first/last name

TODO: Extract initials

TODO: Format in title case
"""

# name = input("Enter your name here: ")
# initials = name.upper().split()
# print(f"Your Initials is: {initials[0][0]} {initials[1][0]}")

"""
String Concatenation Practice
Context: Build sentences by joining multiple string inputs together.

Input: Name = "Sayan", Age = "26", Hobby = "coding"

Output: "My name is Sayan, I am 26 and I love coding."

TODO: Collect inputs

TODO: Concatenate into sentence

TODO: Print formatted output
"""

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# hobby = input("Enter your hobby: ")
# print(f"My name is {name.capitalize()}, I am {age} year old and I love {hobby}")

"""
Password Strength Checker
Context: Use string validation functions to check if a password is strong.

Input: "abc12345"

Output: "Strong password"

TODO: Check length

TODO: Check letters/numbers

TODO: Print strength result

"""
# password = input("Enter your password: ")

# # checks:
# if len(password) < 8:
#     print("Your password is to small")

# else:
#     if password.isdigit():
#         print("Your password is weak")

#     elif password.isalpha():
#         print("Your password is weak")

#     elif password.isalnum():
#         print("Your password is Strong")

"""
Email Formatter
Context: Practice cleaning and validating email addresses.

Input: " Sayan@GMAIL.com "

Output: "sayan@gmail.com"

TODO: Remove spaces

TODO: Convert to lowercase

TODO: Validate with @ and .

"""
# email = input("Enter your email: ")
# clean_email = email.lower().strip()

# if "@" in clean_email:
#     print(clean_email)

# else:
#     print("invalid email")

"""
Custom Formatter
Context: Reformat structured strings (like filenames) into readable formats.

Input: "Report_2026_final.csv"

Output: "Report (Final) - 2026"

✅ Split parts

✅ Rearrange order

✅ Format output

"""
# input_text = "Report_2026_final.csv"
# output = input_text.replace(".", "_").split("_")

# type = output[0].capitalize()
# version = output[2].capitalize()
# year = output[1]

# print(f"{type} ({version}) - {year}")


"""
You are given a messy list of company file names. The list contains duplicates, inconsistent casing, extra spaces, and mixed extensions (.txt, .tmp, .csv).

Your tasks:

Todo: Remove leading/trailing spaces.

Todo: Remove duplicates.

Todo: Convert all extensions to .csv (replace .txt and .tmp).

Todo: Normalize casing (all lowercase or all uppercase).

Todo: Ensure the final output is a clean list of unique file names.

"""

files = [
    " budget.csv ", "Budget.CSV", "p&l.csv", "P&L.txt", "cashflow.tmp",
    "   revenue.csv", "Revenue.CSV", "expenses.txt", "Expenses.csv",
    "forecast.tmp", "Forecast.CSV", "balanceSheet.csv", "balancesheet.TXT",
    "profit_loss.csv", "Profit_Loss.tmp", "audit.csv", "Audit.CSV",
    "tax.txt", "Tax.CSV", "budget.csv"
]

clean = ""

for f in files:
    # Cleaning:
    f = f.strip().lower().replace(".txt", ".csv").replace(".tmp", ".csv")

    # Checking duplicates:
    if f not in clean:
        clean += f + ","

clean_list = [f for f in clean.split(",") if f != ""]
print(clean_list)
