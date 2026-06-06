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

# Function to add a new contact to the contacts dictionary, checking for duplicates and ensuring that the contact name is unique before adding the new contact information.
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

# Function to search for contacts by name or phone number, returning a list of matching contacts based on the search term provided by the user.
def search_contact(contacts, search_term):
    search_term_lower = search_term.lower()
    results = []
    for name, info in contacts.items():
        if search_term_lower in name.lower() or search_term_lower in info["phone"].lower():
            results.append((name, info))
    return results

# Function to update an existing contact's information based on the contact name, the field to update (phone, email, or city), and the new value provided by the user, ensuring that the contact exists and that the specified field is valid before making the update.
def update_contact(contacts, name, field, new_value):
    if name not in contacts:
        print(f"Contact '{name}' not found.")
        return False

    if field not in ["phone", "email", "city"]:
        print("Field must be 'phone', 'email', or 'city'.")
        return False

    contacts[name][field] = new_value
    return True

# Function to delete a contact from the contacts list on the name given from user, but won't delete if the contact doesn't exist and will return a message to the user indicating that the contact was not found. If the contact is successfully deleted, it will return True.
def delete_contact(contacts, name):
    if name not in contacts:
        print(f"Contact '{name}' not found.")
        return False

    del contacts[name]
    return True

# Function to view all contacts in the contacts dictionary, displaying each contact's name, phone number, email, and city in a formatted manner for easy reading by the user.
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

# Function to display the menu options to the user for the contact book application, allowing them to choose from adding a contact, searching for a contact, updating a contact, deleting a contact, viewing all contacts, or exiting the application.
def print_menu():
    print("\nContact Book App")
    print("1. Add a contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. View all contacts")
    print("6. Exit")

# Main loop to display the menu and handle user choices for the contact book application, allowing users to interact with the application by selecting options from the menu and performing actions such as adding, searching, updating, deleting, and viewing contacts based on their input.
while True:
    print_menu()
    choice_input = input("Enter your choice: ").strip()
# Handle user choices for adding a contact, searching for a contact, updating a contact, deleting a contact, viewing all contacts, and exiting the application based on the user's input.
    if choice_input == "1":
        name = input("Enter contact name: ").strip()
        phone = input("Enter contact phone: ").strip()
        email = input("Enter contact email: ").strip()
        city = input("Enter contact city: ").strip()
        if add_contact(contacts, name, phone, email, city):
            print(f"Contact '{name}' added successfully!")
# Handle searching for a contact by prompting the user for a search term (name or phone number) and displaying the search results in a formatted manner, showing the contact's name, phone number, email, and city for each matching contact found in the contacts dictionary.
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
# Handle updating a contact by prompting the user for the contact name, the field to update (phone, email, or city), and the new value, and then calling the update_contact function to make the necessary updates to the contact's information in the contacts dictionary.
    elif choice_input == "3":
        name = input("Enter contact name to update: ").strip()
        field = input("Enter field to update (phone/email/city): ").strip().lower()
        new_value = input(f"Enter new value for {field}: ").strip()
        if update_contact(contacts, name, field, new_value):
            print(f"Contact '{name}' updated successfully!")
# Handle deleting a contact by prompting the user for the contact name and calling the delete_contact function to remove the contact from the contacts dictionary, providing feedback to the user about whether the deletion was successful or if the contact was not found.
    elif choice_input == "4":
        name = input("Enter contact name to delete: ").strip()
        if delete_contact(contacts, name):
            print(f"Contact '{name}' deleted successfully!")
# Handle viewing all contacts by calling the view_all_contacts function, which will display all the contacts in the contacts dictionary in a formatted manner, showing each contact's name, phone number, email, and city for easy reading by the user.
    elif choice_input == "5":
        print("All contacts:")
        view_all_contacts(contacts)
# Handle exiting the application by breaking out of the main loop and displaying a goodbye message to the user.
    elif choice_input == "6":
        print("Exiting the app. Goodbye!")
        break
# Handle invalid menu choices by prompting the user to enter a valid option from the menu if they enter an invalid choice that does not correspond to any of the defined options.
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")

    
       