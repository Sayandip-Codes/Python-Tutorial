"""
Problem Statement:  
Write a Python program that validates the quality and correctness of a password based on the following rules:

TODO: Must not be empty

TODO: Must be at least 8 characters long

TODO: Must include at least 1 uppercase letter

TODO: Must include at least 1 lowercase letter

TODO: Must not be the same as the email

TODO: Must not contain any spaces

TODO: Must start and end with a letter or digit

🎯 Requirements Checklist
Your program should:

TODO: Accept both email and password as input.

TODO: Validate the password against all rules.

TODO: Print whether the password is Valid or Invalid.

TODO: If invalid, print which rule(s) failed.

"""
email = "sayan@gmail.com"
password = "hjjsjsssksslAs"
is_valid = True

# TODO: Must not be empty:
if password == "":
    print("Password must not be empty!")
    is_valid = False

# TODO: Must not contain any spaces
if " " in password:
    print("Password must not contain any spaces!")
    is_valid = False

# TODO: Must be at least 8 characters long
if not (len(password) >= 8):
    print("Password mst be at least 8 characters long")
    is_valid = False

# TODO: Must not be the same as the email
if password == email:
    print("Password must not be the same as the email")
    is_valid = False

# TODO: Must start and end with a letter or digit
if not (password[0].isalnum() and password[-1].isalnum()):
    print("Password ust start and end with a letter or digit")
    is_valid = False

# TODO: Must include at least 1 uppercase letter
if password == password.lower():
    print("Password must include at least 1 uppercase letter")
    is_valid = False

# TODO: Must include at least 1 lowercase letter
if password == password.upper():
    print("Password ust include at least 1 lowercase letter!")
    is_valid = False

# TODO: All checks passed:
if is_valid:
    print("Password is valid!")
