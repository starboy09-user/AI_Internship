from datetime import date

# Input birth date
birth_year = int(input("Enter birth year: "))
birth_month = int(input("Enter birth month: "))
birth_day = int(input("Enter birth day: "))

# Current date
today = date.today()

# Calculate age
age = today.year - birth_year

# Adjust if birthday hasn't occurred yet this year
if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

# Display result
print("Your age is:", age)