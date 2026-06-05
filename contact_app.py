print(int(input("""
      Contact Book App
      1. Add a contact
      2. Search contact
      3. Update contact
      4. Delete contact
      5. View all contacts
      6. Exit
                
      """)))

input = input("Enter your choice: ")

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

if input == "1":

    contacts = []

    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email: ")
    city = input("Enter contact city: ")
    add_contact(contacts, name, phone, email, city)
    




















if input == "6":
    print("Exiting the app. Goodbye!")

    