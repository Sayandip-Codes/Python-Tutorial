"""
TODO: Check if a user's name is not empty and the age is greater than or equal to 18

TODO: Check if a user's password is at least 8 characters long and does not contain spaces

TODO: Check if a user email is not empty, contains '@' and endswith '.com'

TODO: Check if a username is a string, is not None, and is longer than 5 characters 

TODO: Check if the user is either an admin or a moderator, and they're not banned or they've verified their email

"""
print("=" * 45)

username = input("Enter name: ")
age = int(input("Enter age: "))
password = input("Enter password: ")
email = "sayan@gmail.com"
domain = email.split("@")[-1]
banned_domain = ["spam.com", "fake.org", "tempmail.com"]
user_role = input("Select your role: ")

# TODO 01:
print(username is not None and username != "" and len(username) > 5)

# # TODO 02:
# print(age >= 18)

# # TODO 03:
print(len(password) >= 8 and " " not in password)

# TODO 04:admin
print((email != "" and email.endswith(".com")) and ('@' in email))

# TODO 05:
print(domain in banned_domain)
print(user_role.lower() == "admin" or user_role.lower() == "moderator")

print("=" * 45)
