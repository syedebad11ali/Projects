from datetime import datetime

print("How Old Are They?")

birth_year = int(input("Enter your birth year: "))
current_year = datetime.now().year
age = current_year - birth_year

print(f"You are {age} years old.")
