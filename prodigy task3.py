import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)

def add_contact(name, phone, email):
    contacts = load_contacts()
    if name in contacts:
        print(f"Contact {name} already exists.")
    else:
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} added successfully.")
        save_contacts(contacts)

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
    else:
        for name, contact in contacts.items():
            print(f"{name}: {contact['phone']}, {contact['email']}")

def edit_contact(name, **edited_fields):
    contacts = load_contacts()
    if name not in contacts:
        print(f"Contact {name} not found.")
    else:
        for field, new_value in edited_fields.items():
            contacts[name][field] = new_value
        print(f"Contact {name} edited successfully.")
        save_contacts(contacts)

def delete_contact(name):
    contacts = load_contacts()
    if name not in contacts:
        print(f"Contact {name} not found.")
    else:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
        save_contacts(contacts)

def main():
    while True:
        print("\nContact Management System")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Edit contact")
        print("4. Delete contact")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            add_contact(name, phone, email)
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            name = input("Enter contact name to edit: ")
            for field in ['phone', 'email']:
                new_value = input(f"Enter new {field} for {name}: ")
                edit_contact(name, **{field: new_value})
        elif choice == 4:
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()