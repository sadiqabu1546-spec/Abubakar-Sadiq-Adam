import datetime

NOTES_FILE = "my_diary_notes.txt"

def add_note():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note_content = input("Enter your diary entry: ")
    
    with open(NOTES_FILE, 'a') as file:
        file.write(f"[{timestamp}] {note_content}\n")
    print("Note added successfully!")

def view_notes():
    try:
        with open(NOTES_FILE, 'r') as file:
            print("\n--- Your Diary Entries ---")
            lines = file.readlines()
            if not lines:
                print("Your diary is empty.")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("No diary entries found yet. Start by adding one!")

def main_menu():
    while True:
        print("\n--- Diary App Menu ---")
        print("1. Add a new note")
        print("2. View all notes")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            print("Exiting Diary App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
