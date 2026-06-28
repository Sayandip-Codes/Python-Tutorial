"""
Turn messy string into a single clean summary with name, role, and age

"968-Maria,( d@t@ Engineer ) ;; 27y   "

clean string: 
name: maria | role: data engineer | age: 27

"""

# Brute Force:
unclean_str = "968-Maria,( d@t@ Engineer ) ;; 27y   "

clean_str = unclean_str.replace("968", "").replace(",", "").replace(
    "@", "a").replace("(", "").replace(")", "").replace(";", "").replace("y", "").replace("-", "").lower().strip().split()


print(
    f"name: {clean_str[0]} | role: {clean_str[1] + " " + clean_str[2]} | age: {clean_str[3]}")

print("=" * 50)


# Clean Approach:
unclean_str2 = "968-Maria,( d@t@ Engineer ) ;; 27y   "

# Step - 01: Cleaning
clean_str1 = (
    unclean_str.replace("968", "")
    .replace(",", "")
    .replace(
        "@", "a")
    .replace("(", "")
    .replace(")", "")
    .replace(";", "")
    .replace("y", "")
    .replace("-", "")
    .lower()
    .strip())

# Step - 02: breaking into parts
parts = clean_str1.split()

# Step - 03:  Assigning values
name = parts[0]
role = " ".join(parts[1:-1])
age = parts[3]


print(
    f"name: {name} | role: {role} | age: {age}")
