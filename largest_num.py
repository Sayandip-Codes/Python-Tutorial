numbers = [
    42, 7, 89, 15, 3, 56, 23, 91, 12,
    67, 34, 5, 78, 29, 1, 60, 18, 84, 9, 50
]

# Sorting the list will automatically send the largest number to the last index
numbers.sort()
print(numbers)

# printing largest number
largest_num = numbers[-1]
print(f"Largest number = {largest_num}")

# Best approach:
print(f"Best approach: {max(numbers)}")

# Best approach for lowest number:
print(f"Best approach: {min(numbers)}")
