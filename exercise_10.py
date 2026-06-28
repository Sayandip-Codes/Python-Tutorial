
"""
Check whether any filename appears more than once
Todo: print "Duplicate found" if a duplicate exists,
Todo: otherwise print "All files are unique"
"""

file_list = [
    'report.xlsx',
    'report.csv',
    'summary.docx',
    'report.csv',
    'data.csv'
]

# flag:
duplicate_found = False

# Outer loop picks each file:
for i in range(len(file_list)):
    # Inner loop compares it with all later files:
    for j in range(i + 1, len(file_list)):
        # If a match is found → mark duplicate_found = True and break inner loop:
        if file_list[i] == file_list[j]:
            duplicate_found = True
            break
    # If duplicate is found then break outer loop as well:
    if duplicate_found:
        break


# After loops end, print the result:
if duplicate_found:
    print("\nDuplicate Found!\n")
else:
    print("\nAll files are unique\n")
