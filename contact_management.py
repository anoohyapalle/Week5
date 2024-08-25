import pickle

def read_contacts_from_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            contacts = [line.strip().split(',') for line in file]
        return [{'name': name, 'phone': phone} for name, phone in contacts]
    except FileNotFoundError:
        print(f"{file_name} not found. Starting with an empty contact list.")
        return []

def write_contacts_to_text_file(file_name, contacts):
    with open(file_name, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']}\n")

def save_contacts_to_binary_file(file_name, contacts):
    with open(file_name, 'wb') as file:
        pickle.dump(contacts, file)

def load_contacts_from_binary_file(file_name):
    try:
        with open(file_name, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f"{file_name} not found. Starting with an empty contact list.")
        return []

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts.append({'name': name, 'phone': phone})
    print(f"Contact {name} added.")

def remove_contact(contacts):
    name = input("Enter the name of the contact to remove: ")
    contacts[:] = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    print(f"Contact {name} removed if it existed.")

def display_contacts(contacts):
    if contacts:
        print("Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No contacts to display.")


def main():
    contacts = []
    text_file = 'contacts.txt'
    binary_file = 'contacts.dat'

    while True:
        print("\nContact Management System")
        print("1. Load contacts from text file")
        print("2. Save contacts to text file")
        print("3. Load contacts from binary file")
        print("4. Save contacts to binary file")
        print("5. Add contact")
        print("6. Remove contact")
        print("7. Display contacts")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            contacts = read_contacts_from_text_file(text_file)
        elif choice == '2':
            write_contacts_to_text_file(text_file, contacts)
        elif choice == '3':
            contacts = load_contacts_from_binary_file(binary_file)
        elif choice == '4':
            save_contacts_to_binary_file(binary_file, contacts)
        elif choice == '5':
            add_contact(contacts)
        elif choice == '6':
            remove_contact(contacts)
        elif choice == '7':
            display_contacts(contacts)
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
