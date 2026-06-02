student = {
    "name": "Vibhu",
    "age": 22,
    "course": "BSc CA & IT"
}

print("Original Dictionary:")
print(student)

# Add
student["city"] = "Vadodara"
print("\nAfter Add:")
print(student)

# Update
student["age"] = 21
print("\nAfter Update:")
print(student)

# Delete
del student["city"]
print("\nAfter Delete:")
print(student)

# Display using loop
print("\nDisplay All Data:")
for key, value in student.items():
    print(key, ":", value)