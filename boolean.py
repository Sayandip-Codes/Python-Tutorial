
# ? Boolean:
print(True)
print(False)
print(type(False))
print(bool(123))
print(bool("Hey"))
print(bool())
print(bool(0))
print(bool(1))
print(bool(""))
print(bool(None))

print("=" * 45)

# Function any() and all():
email = ""
phone = "7980-425-560"
username = ""

# TODO: Allow if any field is filled:
print(f"Any field is filled? : {any([email, phone, username])}")

# TODO: Allow only if all field is filled:
print(f"All fields are filled? : {all([email, phone, username])}")

print("=" * 45)

"""
Comparison operators:
It compares two values and return True or False based on the result.
"""

print(f"Equal: {10 == 10}")
print(f"Equal: {10 != 10}")
print(f"less: {7 > 3}")
print(f"Greater: {7 >= 3}")
print(f"less-Equal: {3 < 7}")
print(f"Greater-Equal: {7 <= 7}")
print(f"{"a" == "b"}")
print(f"{"a" != "A"}")

# TODO: Is age between 18 and 30
age = 26
print(f"Age eligible: {18 <= age <= 30}")


print("=" * 45)

"""
Logical operators:
Used to combine multiple boolean expressions.
"""

# AND operator: when both the condition are true
print(3 > 2 and 3 < 5)
print(2 > 6 and 1 < 5)

# TODO: Checking user credentials before login
email = True
password = False

print(email and password)


# OR operator: when one condition is true
print(2 > 6 or 1 < 5)
print("a" == "A" or "b" != "B")

# TODO: Check if the system is under pressure
# Computer one:
com1_cpu_usage = 70
com1_memory_usage = 95

# Computer two:
com2_cpu_usage = 70
com2_memory_usage = 56

print(f"Computer one: {com1_cpu_usage > 90 or com1_memory_usage > 90}")
print(f"Computer two: {com2_cpu_usage > 90 or com2_memory_usage > 90}")

# NOT operator: will turn true to false and false to true
print(not 3 > 2)
print(not True)
print(not False)
print(not not False)

print("=" * 45)

# Execution order:
# and has higher precedence than or, thats why we use parenthesis to have the control

# TODO: Allow access only if the user is logged in
# TODO: or they are guest
# TODO: but they must not banned

is_logged_in = False
is_guest = True
is_banned = True

print("Login status: ", (is_logged_in or is_guest) and not is_banned)

print("=" * 45)

# Membership operator: check if the mentioned value is present in the data or not
print("a" and "f" in "Sayandip")
print("m" not in "sayan")
# TODO: Validate that the domain is not on the banned list

domain = "fake.org"
banned_domain = ["spam.com", "fake.org", "tempmail.com"]

print("Is domain safe: ", not domain in banned_domain)

print("=" * 45)

# Identity operator:
x = ['a', 'b', 'c']
y = ['a', 'b', 'c']

""" 
So in case of objects the python goes and builds separate IDs, so the is() will return false
"""
print(x == y)
print(x is y)

x = 10
y = 10

""" 
So in case of single or same values the python goes and build same ID, so the is() will return true
"""
print(x == y)
print(x is y)

# TODO: Make sure the email exists, and it's not empty
email = input("Enter your email: ")
print(email is not None and email is not "")

