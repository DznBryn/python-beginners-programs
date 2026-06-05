contacts = {
    "Maya Johnson": {
        "phone": "201-555-0148",
        "email": "maya.johnson@example.com",
        "city": "Jersey City"
    },
    "Ethan Brown": {
        "phone": "973-555-0199",
        "email": "ethan.brown@example.com",
        "city": "Newark"
    },
    "Sophia Lee": {
        "phone": "212-555-0182",
        "email": "sophia.lee@example.com",
        "city": "New York"
    },
    "Noah Davis": {
        "phone": "908-555-0115",
        "email": "noah.davis@example.com",
        "city": "Elizabeth"
    },
    "Ava Wilson": {
        "phone": "551-555-0164",
        "email": "ava.wilson@example.com",
        "city": "Hoboken"
    }
}


def add_contact(contacts, name, phone, email, city):
    if name in contacts:
        print(f"A contact named '{name}' already exists. Use update instead.")
        return False

    contacts[name] = {
        "phone": phone,
        "email": email,
        "city": city
    }
    return True


def search_contact(contacts, search_term):
    search_term_lower = search_term.lower()
    results = []
    for name, info in contacts.items():
        if search_term_lower in name.lower() or search_term_lower in info["phone"].lower():
            results.append((name, info))
    return results


def update_contact(contacts, name, field, new_value):
    if name not in contacts:
        print(f"Contact '{name}' not found.")
        return False

    if field not in ["phone", "email", "city"]:
        print("Field must be 'phone', 'email', or 'city'.")
        return False

    contacts[name][field] = new_value
    return True


def delete_contact(contacts, name):
    if name not in contacts:
        print(f"Contact '{name}' not found.")
        return False

    del contacts[name]
    return True


def view_all_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"  Phone: {info['phone']}")
        print(f"  Email: {info['email']}")
        print(f"  City: {info['city']}")
        print("-")


def print_menu():
    print("\nContact Book App")
    print("1. Add a contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. View all contacts")
    print("6. Exit")


while True:
    print_menu()
    choice_input = input("Enter your choice: ").strip()

    if choice_input == "1":
        name = input("Enter contact name: ").strip()
        phone = input("Enter contact phone: ").strip()
        email = input("Enter contact email: ").strip()
        city = input("Enter contact city: ").strip()
        if add_contact(contacts, name, phone, email, city):
            print(f"Contact '{name}' added successfully!")

    elif choice_input == "2":
        search_term = input("Enter name or phone to search: ").strip()
        results = search_contact(contacts, search_term)
        if results:
            print("Search results:")
            for name, info in results:
                print(f"Name: {name}")
                print(f"  Phone: {info['phone']}")
                print(f"  Email: {info['email']}")
                print(f"  City: {info['city']}")
                print("-")
        else:
            print("No contacts found.")

    elif choice_input == "3":
        name = input("Enter contact name to update: ").strip()
        field = input("Enter field to update (phone/email/city): ").strip().lower()
        new_value = input(f"Enter new value for {field}: ").strip()
        if update_contact(contacts, name, field, new_value):
            print(f"Contact '{name}' updated successfully!")

    elif choice_input == "4":
        name = input("Enter contact name to delete: ").strip()
        if delete_contact(contacts, name):
            print(f"Contact '{name}' deleted successfully!")

    elif choice_input == "5":
        print("All contacts:")
        view_all_contacts(contacts)

    elif choice_input == "6":
        print("Exiting the app. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")

    
       