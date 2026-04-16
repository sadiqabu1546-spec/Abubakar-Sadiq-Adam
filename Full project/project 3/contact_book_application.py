# Global dictionary to store contacts
contacts = {}

def add_contact():
    # .strip().title() ensures "  alice  " becomes "Alice"
    name = input("Enter contact name: ").strip().title()
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully.")

def view_contact():
    name = input("Enter name to search: ").strip().title()
    if name in contacts:
        details = contacts[name]
        print(f"\nName: {name}\nPhone: {details['phone']}\nEmail: {details['email']}")
    else:
        print("Error: Contact not found.")

def list_contacts():
    if not contacts:
        print("The contact book is empty.")
        return
    
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"Name: {name} | Phone: {info['phone']}")

def delete_contact():
    name = input("Enter name to delete: ").strip().title()
    # Safety check to prevent KeyError
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Error: Contact does not exist.")

# Main Loop
while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact\n2. View Contact\n3. List All\n4. Delete Contact\n5. Exit")
    
    choice = input("Select an option (1-5): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact()
    elif choice == '3':
        list_contacts()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
