# Type:
name = "Sayandip"
print(type(name))

age = 24
print("Your age is: ", str(age))
age = age + 2
age = str(age)
print(type(age))

# Math:
password = "123ah"
print(len(password))

if len(password) < 8:
    print("password is to short ")
else:
    print("All good")

text = """ 
Python is easy to learn
Python is powerful
Many people love python now
"""

print(text.count("Python"))
print(text.count("python"))

print("=" * 45)

# Transformation:
price = "24,45"
phone = "7980-460-500"
price = "$126,35"

print(price.replace(",", "."))
print(price.replace("$", "").replace(",", "."))
print(phone.replace("-", "/"))
print(phone.replace("-", ""))

path = "C:/Users/Sayandip"
file = "report.csv"
full_file_path = path + "/" + file
print(full_file_path)

print("=" * 45)

# f-string:
name2 = "Sayan"
age2 = 26
is_Student = False

# Old method:
print("My name is " + name2 + "and my age is " +
      str(age2) + "my status as student is " + str(is_Student))

# New method:
print(
    f"My name is {name2} and my age is {age2} my status as student is {is_Student}")
print(f"2 + 6 =  {2 + 6}")

# Split():
ext = "game_app.py"
print(ext.split(".")[1])

stamp = "2026-06-05 02:23 PM"
print(stamp.split("-"))

csv_file = "1234,Sayandip,INDIA,04-01-2000"
print(csv_file.split(","))

print("ha" * 3)

print("=" * 45)

# Extraction:
txt = "Python"

# Extract first character:
print(txt[0])  # positive index
print(txt[-6])  # negative index

# Extract last character:
print(txt[5])  # positive index
print(txt[-1])  # negative index

# Extract 'h' character:
print(txt[3])  # positive index
print(txt[-3])  # negative index


new_date = "08-06-2026"

# Extract year:
print(f"Year: {new_date[6:11]}")  # start: 6th[2] and end: 10th[6]

# Extract month:
print(f"Month: {new_date[3:5]}")

# Extract day:
print(f"Day: {new_date[:2]}")
print(f"Day: {new_date[:-8]}")

print("=" * 45)

# Whitespace cleanup:
lft_space = "    Sayandip"
rgt_space = "Sayandip     "
bth_spaces = "      Sayandip           "

print(f"Left side space removed: {lft_space.lstrip()}")
print(f"Right side space removed: {rgt_space.rstrip()}")
print(f"Both side space removed: {bth_spaces.strip()}")

# Tips:
num_of_spaces = (len(bth_spaces) - len(bth_spaces.strip()))
isClean = (len(bth_spaces) == len(bth_spaces.strip()))

print(f"No. of spaces: {num_of_spaces}")
print(f"Is my data clean? : {isClean}")


print("=" * 45)

# Case converter:
msg = "python programming"

print(msg.lower())
print(msg.upper())
print(msg.capitalize())

print("=" * 45)

search = "Email"
data = "  eMaIl"

# Before formatting:
print(f"Before formatting: {search == data}")

# After formatting:
print(
    f"After formatting: {search.lower().strip() == data.lower().strip()}")

print("=" * 45)

# Searching:
phone = "+49-176-25636"
print(f"Is the number from Germany: {phone.startswith("+49")}")

email = "sayan@gmail.com"
print(f"Does the email have google domain: {email.endswith("gmail.com")}")
print(f"Is it a valid email: {"@" in email}")

url = "https://api.company.com/v1/data"
print(f"Does this url belongs to API: {"/api" in url}")

phone_01 = "+48-176-56236"
phone_02 = "48-654-46326"

print(phone_01[phone_01.find("-")+1:])
print(phone_02[phone_02.find("-")+1:])

print("=" * 45)

# Validation:
state = "WB"
code = "700091"
pswd = "hahha@126"

print(f"Did user entered valid State: {state.isalpha()}")
print(f"Did user entered valid location Code: {code.isnumeric()}")
print(f"Did user entered valid password: {code.isalnum()}")
