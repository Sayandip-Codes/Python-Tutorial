# sys is a built-in Python module that lets you interact with the Python interpreter and system environment.
import sys

# Create 5 variables - each with different data type:
#  - Your age
#  - Your height
#  - Your name
#  - Are you a student
#  - Something with no value yet

# print the values , data types, lengths of all variables:

name = "Sayandip"
age = 26
height = 5.6
isStudent = False
inProgress = None

print("Name: ", name, "Data type: ", type(name), "Size: ", len(name))
print("Age: ", age, "Data type: ", type(age), "Size: ", sys.getsizeof(age))
print("Height: ", height, "Data type: ", type(
    height), "Size: ", sys.getsizeof(height))
print("Student: ", isStudent, "Data type: ", type(
    isStudent), "Size: ", sys.getsizeof(isStudent))
print("Status: ", inProgress, "Data type: ", type(
    inProgress), "Size: ", sys.getsizeof(inProgress))
