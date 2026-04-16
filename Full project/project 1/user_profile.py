name = input("insert your name: ")
age = int(input("how old are you: "))
height_cm = float(input("what is your hieght: "))
is_student = input("Are you a student? (Type 'True' or 'False'): ")

# 5. Convert Height to Inches (cm / 2.54)
height_inches = height_cm / 2.54

# 6. Print formatted User Profile
print("\n--- User Profile ---")
print(f"Name: {name}")
print(f"Age: {age} years")
print(f"Height: {height_cm} cm ({height_inches:.2f} inches)")
print(f"Student: {is_student}")
print("congratulation ")