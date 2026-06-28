# Convert the messy phone number into clean number format with digits only
# +49 (176) 123-4567


phone = "+49 (176) 123-4567"

print("Cleaned phone no.: ", phone.replace("+", "").replace("(", "").replace(")",
      "").replace("-", "").replace(" ", ""))

