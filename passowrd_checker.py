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

def has_uppercase(password):
    if any(char.isupper() for char in password):
        return True
    


def has_lowercase(password):
    if any(char.islower() for char in password):
        return True
    


def has_number(password):
    if any(char.isdigit() for char in password):
        return True
    


def has_special_character(password):
    special_characters = "!@#$%^&*()-+"
    if any(char in special_characters for char in password):
        return True
    


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

def print_menu():
    print("\nPassword Strength Checker")
    print("1. Check password strength")
    print("2. Test sample passwords")
    print("3. Exit")

while True:
    print_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        password = input("Enter a password to check its strength: ").strip()
        strength = check_password_strength(password)
        print(f"Password strength: {strength}")

    elif choice == "2":
        print("\nTesting sample passwords:")
        for pwd in sample_passwords:
            strength = check_password_strength(pwd)
            print(f"Password: {pwd} - Strength: {strength}")

    elif choice == "3":
        print("Exiting Password Strength Checker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 3.")
