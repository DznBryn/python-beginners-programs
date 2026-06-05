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




from random import choice


print(int(input("""
      Contact Book App
      1. Add a contact
      2. Search contact
      3. Update contact
      4. Delete contact
      5. View all contacts
      6. Exit
                
      """)))

choice = input("Enter your choice: ")

def add_contact(contacts, name, phone, email, city):
   pass
def search_contact(contacts, search_term):
    pass
def update_contact(contacts, name, field, new_value):
    pass
def delete_contact(contacts, name):
    pass
def view_all_contacts(contacts):
    pass

contacts = []

if choice == "1":

    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email: ")
    city = input("Enter contact city: ")
    add_contact(contacts, name, phone, email, city)

    print(f"Contact '{name}' added successfully!")

elif choice == "2":
    

    search_term = input("Enter name or phone to search: ")
    results = search_contact(contacts, search_term)
    if results:
        print("Search results:")
        for contacts in results:
            print(contacts)
    else:
        print("No contacts found.")

elif choice == "3":
    name = input("Enter contact name to update: ")
    field = input("Enter field to update (phone/email/city): ")
    new_value = input(f"Enter new value for {field}: ")
    update_contact(contacts, name, field, new_value)
    print(f"Contact '{name}' updated successfully!")

elif choice == "4":
    name = input("Enter contact name to delete: ")
    delete_contact(contacts, name)
    print(f"Contact '{name}' deleted successfully!")

elif choice == "5":
    print("All contacts:")
    view_all_contacts(contacts)



    




















if choice == "6":
    print("Exiting the app. Goodbye!")

    