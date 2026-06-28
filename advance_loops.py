"""
? Break:
- It stops the loop immediately
- It jumps out and ends
- The loop right away
- Mostly used for Critical Level Risk
    • Cost
    • Security
    • Integrity
"""

names = ["John", "Max", "", "Sayan"]
for name in names:
    if name == "":
        print("No Name")
        break
    else:
        print(f"Name: {name}")

print("=" * 45)

"""
? Skip:
- It skips one loop cycle without stopping the loop
- Skip this one and go to next
- Mostly used for Medium Level Risk
    • Bad rows
    • Empty Files/Data
    • Skip Special Cases
"""
for name in names:
    if name == "":
        print("Skipped")
        continue
    else:
        print(f"Name: {name}")


print("=" * 45)

"""
? Pass:
- It is a placeholder where nothing happens
- For now.. just keep going and do nothing
- Mostly used for placeholder
    • Planning
"""
for name in names:
    if name == "":
        # pass  # todo: Handle blank value
        name = name.replace("", "Unknown")
    print(f"Name: {name}")


print("=" * 45)


# Todo: loop thru a list of days and print only the working days, skipping the weekends
days = ["Mon", "Tue", "Sun", "Wed", "Thus", "Sat", "Fri"]
weekend = ["sat", "sun"]
for day in days:
    if day.lower() in weekend:
        print("Weekends")
        continue
    else:
        print(f"Workday: {day}")

print("=" * 45)

# Todo: Scan emails to block unsafe data from entering your system
emails = [
    "data@gmail.com",
    "sayan@outlook.de",
    "DROP TABLE USERS;",
    "maria@gmail.com"
]

for email in emails:
    if ";" in email:
        print("Warring!: SQL Injection Found : Shutdown Protocol Activated")
        break

    print(f"Processing Email: {email}")

print("=" * 45)

"""
? Else in loop:
- Runs a block of code only if the loop finishes naturally
- Loop completed without breaks
"""
lists = [1, 21, 3, 9, 5]
for i in lists:
    if i % 2 == 0:
        print(f"Even No. : {i}")
        break
else:
    print("All No. are odd")

print("=" * 45)

# Todo: Check for names in a list:
names = ["Kamara", "Monica", None, "Barnali"]

for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All names are available")


print("=" * 45)


# Todo: Check if all file extensions are csv or not:

files = [
    "Budget.csv", "Planner.txt",
    "Breakeven_report.csv", "Q1_report.csv",
    "Q1_report.txt"]

for file in files:
    if not file.endswith("csv"):
        print(f"{file} is not in csv format")
        break
else:
    print("All files are in csv format")


print("=" * 45)


# Nested loop:
for x in range(3):  # Outer loop
    for y in range(2):  # Inner loop
        for z in range(2):  # 2nd inner inner loop
            print(f"({x}, {y}, {z})")

print("=" * 45)
"""
? Use cases of nested loops are:
- Crossing data → handling combinations, comparisons, and pairwise checks.

- Navigating hierarchy → moving through multi-level structures like grids, trees, or nested categories.
"""

"""
? Crossing data:

- Comparing every element with every other element (e.g., duplicate detection in file lists).

- Generating combinations or pairs (like (i, j) in a dataset).

- Useful in algorithms such as bubble sort, insertion sort, or brute-force searches.
"""
colors = ['red', 'blue', 'green']
sizes = ['S', 'M', 'L']

for color in colors:
    for size in sizes:
        print(f"{color} = {size}")

print("=" * 45)

"""
? Navigating hierarchy

- Traversing multi‑level structures: rows × columns in a matrix, days × periods in a timetable, or parent × child nodes in a tree.

- Printing structured patterns (stars, grids, tables).

- Iterating through nested folders or categories in file systems.
"""

# Todo: Use nested loops to create csv files for each year, month, and day "report_yyyy_mm_dd.csv";
years = [2026, 2027]
months = ['Jan', 'Feb']
days = range(1, 29)

for y in years:
    for m in months:
        for d in days:
            print(f"report_{y}_{m}_{d}.csv")


print("=" * 45)


# Todo: Use nested loops to write SQL query "SELECT count(*) FROM customers WHERE id IS NULL";
tables = ['customers', 'orders', 'products', 'prices']
column = [
    'id', 'create_date', 'shipment_items',
    'invoices', 'payments', 'return', 'refunds',
    'reviews', 'carts', 'cart_items'
]

for t in tables:
    for col in column:
        print(f"SELECT count(*) FROM {t} WHERE {col} IS NULL;")
