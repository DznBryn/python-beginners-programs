sample_passwords = [
    "hello",
    "python123",
    "Python123",
    "Python123!",
    "MySecurePass2026!",
    "PASSWORD",
    "pass word 123",
    "Code@17"
]
# Checks if the password has any uppercase letters

def has_uppercase(password):
    if any(char.isupper() for char in password):
        return True
    
# Checks if the password has any lowercase letters

def has_lowercase(password):
    if any(char.islower() for char in password):
        return True
    
# Checks if the password has any numbers

def has_number(password):
    if any(char.isdigit() for char in password):
        return True
    
# Checks if the password has any special characters

def has_special_character(password):
    special_characters = "!@#$%^&*()-+"
    if any(char in special_characters for char in password):
        return True
    

# Checks the strength of the password based on defined criteria
def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    if not has_uppercase(password):
        return "Weak"
    if not has_lowercase(password):
        return "Weak"
    if not has_number(password):
        return "Weak"
    if not has_special_character(password):
        return "Weak"
    return "Strong"
# Displays the menu options to the user
def print_menu():
    print("\nPassword Strength Checker")
    print("1. Check password strength")
    print("2. Test sample passwords")
    print("3. Exit")
# Main loop to display the menu and handle user choices
while True:
    print_menu()
    choice = input("Enter your choice: ").strip()
# Checks the strength of a user-entered password and displays the result
    if choice == "1":
        password = input("Enter a password to check its strength: ").strip()
        strength = check_password_strength(password)
        print(f"Password strength: {strength}")
# Tests the strength of predefined sample passwords and displays the results
    elif choice == "2":
        print("\nTesting sample passwords:")
        for pwd in sample_passwords:
            strength = check_password_strength(pwd)
            print(f"Password: {pwd} - Strength: {strength}")
# Exits the program when the user chooses to do so
    elif choice == "3":
        print("Exiting Password Strength Checker. Goodbye!")
        break
# Handles invalid menu choices by prompting the user to enter a valid option
    else:
        print("Invalid choice. Please enter a number from 1 to 3.")
