# Password Strength Checker
password = input("Enter your password: ")

# 1. Initialize Flags
has_min_length = len(password) >= 12
has_uppercase = False
has_lowercase = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

# 2. Check each character
for char in password:
    if char.isupper():
        has_uppercase = True
    if char.islower():
        has_lowercase = True
    if char.isdigit():