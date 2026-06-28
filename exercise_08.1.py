"""
Problem Statement:  
Write a Python program that validates the quality and correctness of an email address based on the following rules:

TODO: Must not be empty

TODO: Must contain both . and @

TODO: Must contain exactly one @

TODO: Must end with .com, .org, or .net

TODO: Must not be longer than 254 characters

TODO: Must start and end with a letter or digit

"""
"""
Test cases:
"  "
sayangmail@
sayan.gmail
sayan@gmail.spam
sayan@gmail.net-
sayan@gmail@.com

"""


email = input("Enter email: ")
flag = True

# Cleaning the input:
email = email.strip()

# Checks:
# TODO: Must not be empty:
if email == "":
    print("Email cannot be empty!")
    flag = False

# TODO: Must contain both . and @:
if not ('.' in email and '@' in email):
    print("Email must contain both . and @")
    flag = False

# TODO: Must contain exactly one @:
if email.count('@') != 1:
    print("Email must contain exactly one @")
    flag = False

# TODO: Must end with .com, .org, or .net:
if not (email.endswith((".com", ".org", ".net"))):# using sequence structure to store multiple data at once.
    print("Email must end with .com, .org, or .net")
    flag = False

# TODO: Must not be longer than 254 characters:
if len(email) > 254:
    print("Email must not be longer than 254 characters")
    flag = False

# TODO: Must start and end with a letter or digit:
if not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
    flag = False

# TODO: All checks cleared:
if flag:
    print("Email is valid!")
