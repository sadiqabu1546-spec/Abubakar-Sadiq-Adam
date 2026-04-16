# The main record system
students = {}

def add_student(sid, name, major, gpa):
    # Creating a nested dictionary as the value
    students[sid] = {
        "name": name,
        "major": major,
        "gpa": float(gpa)
    }
    print(f"Student {sid} added successfully.")

def view_student(sid):
    # Check if ID exists to avoid a KeyError
    if sid in students:
        info = students[sid]
        print(f"ID: {sid} | Name: {info['name']} | Major: {info['major']} | GPA: {info['gpa']}")
    else:
        print("Error: Student ID not found.")

def update_gpa(sid, new_gpa):
    if sid in students:
        students[sid]["gpa"] = float(new_gpa)
        print(f"GPA updated for Student {sid}.")
    else:
        print("Error: Cannot update. ID does not exist.")

def list_all_students():
    print("\n--- Current Student Records ---")
    # Using .items() to get both the key and the inner dictionary
    for sid, info in students.items():
        print(f"[{sid}] {info['name']} - {info['major']} (GPA: {info['gpa']})")

# Testing the system
add_student("S101", "halima", "Computer Science", 3.8)
add_student("S102", "Chidi", "Mechanical Engineering", 3.5)

list_all_students()

update_gpa("S101", 3.9)
view_student("S101")
