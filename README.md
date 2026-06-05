# Beginner Python Practice Programs

This repo contains three beginner-friendly Python console programs based on early Python concepts: variables, data types, strings, control flow, lists, loops, functions, dictionaries, nested data, function parameters, and return values.

Programs included:

1. Personal Budget Tracker
2. Password Strength Checker
3. Contact Book App

---

## 1. Personal Budget Tracker

### Goal

Build a console app that helps a user track income, expenses, spending categories, and remaining balance.

### Skills Practiced

- Variables
- Numbers and strings
- Lists
- Dictionaries
- Loops
- Functions
- Function return values
- Conditional logic

### Program Requirements

The program should allow the user to:

- Add income
- Add an expense
- View all expenses
- View total expenses
- View spending by category
- View remaining balance
- Exit the program

### Suggested Data Structure

```python
budget_data = {
    "income": 0,
    "expenses": []
}
```

Each expense can be stored as a dictionary:

```python
{
    "name": "Groceries",
    "category": "Food",
    "amount": 85.50
}
```

### Seed Data

```python
budget_data = {
    "income": 3200.00,
    "expenses": [
        {
            "name": "Rent",
            "category": "Housing",
            "amount": 1450.00
        },
        {
            "name": "Groceries",
            "category": "Food",
            "amount": 185.75
        },
        {
            "name": "Gas",
            "category": "Transportation",
            "amount": 52.40
        },
        {
            "name": "Internet Bill",
            "category": "Utilities",
            "amount": 69.99
        },
        {
            "name": "Gym Membership",
            "category": "Health",
            "amount": 30.00
        }
    ]
}
```

### Example Menu

```text
Personal Budget Tracker
1. Add income
2. Add expense
3. View all expenses
4. View total expenses
5. View spending by category
6. View remaining balance
7. Exit
```

### Suggested Functions

```python
def add_income(budget_data, amount):
    pass


def add_expense(budget_data, name, category, amount):
    pass


def get_total_expenses(budget_data):
    pass


def get_remaining_balance(budget_data):
    pass


def get_expenses_by_category(budget_data):
    pass
```

### Challenge

Create a function that returns a full summary dictionary:

```python
{
    "income": 3200.00,
    "total_expenses": 1788.14,
    "remaining_balance": 1411.86,
    "categories": {
        "Housing": 1450.00,
        "Food": 185.75,
        "Transportation": 52.40,
        "Utilities": 69.99,
        "Health": 30.00
    }
}
```

---

## 2. Password Strength Checker

### Goal

Build a console app that checks how strong a password is based on common password rules.

### Skills Practiced

- Strings
- Loops
- Logical operators
- Control flow
- Functions
- Function parameters
- Function return values

### Program Requirements

The program should ask the user for a password and check whether it:

- Has at least 8 characters
- Has at least 1 uppercase letter
- Has at least 1 lowercase letter
- Has at least 1 number
- Has at least 1 special character

The program should return:

- A strength score
- A strength label
- Suggestions for improvement

### Suggested Data Structure

```python
password_result = {
    "password": "",
    "score": 0,
    "strength": "",
    "suggestions": []
}
```

### Seed Data

Use this list to test your program:

```python
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
```

### Expected Example Results

```python
expected_results = [
    {
        "password": "hello",
        "expected_strength": "Weak",
        "notes": "Too short, missing uppercase, number, and special character."
    },
    {
        "password": "python123",
        "expected_strength": "Medium",
        "notes": "Has lowercase and numbers, but missing uppercase and special character."
    },
    {
        "password": "Python123!",
        "expected_strength": "Strong",
        "notes": "Meets all basic password requirements."
    }
]
```

### Example Menu

```text
Password Strength Checker
1. Check a password
2. Test sample passwords
3. Exit
```

### Suggested Functions

```python
def has_uppercase(password):
    pass


def has_lowercase(password):
    pass


def has_number(password):
    pass


def has_special_character(password):
    pass


def check_password_strength(password):
    pass
```

### Challenge

Update `check_password_strength()` so it returns a dictionary:

```python
{
    "score": 5,
    "strength": "Strong",
    "suggestions": []
}
```

---

## 3. Contact Book App

### Goal

Build a console app that stores contacts and allows the user to add, search, update, delete, and view contacts.

### Skills Practiced

- Dictionaries
- Nested dictionaries
- Strings
- Lists
- Loops
- Functions
- Function parameters
- Function return values
- Conditional logic

### Program Requirements

The program should allow the user to:

- Add a new contact
- Search for a contact
- Update a contact
- Delete a contact
- View all contacts
- Exit the program

### Suggested Data Structure

```python
contacts = {
    "John Carter": {
        "phone": "555-123-4567",
        "email": "john@example.com",
        "city": "Jersey City"
    }
}
```

### Seed Data

```python
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
```

### Example Menu

```text
Contact Book App
1. Add contact
2. Search contact
3. Update contact
4. Delete contact
5. View all contacts
6. Exit
```

### Suggested Functions

```python
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
```

### Challenge

Create a search function that can search by:

- Name
- Phone number
- Email
- City

Example:

```python
def search_contacts(contacts, search_term):
    results = []

    for name, details in contacts.items():
        if search_term.lower() in name.lower():
            results.append({name: details})
        elif search_term.lower() in details["phone"].lower():
            results.append({name: details})
        elif search_term.lower() in details["email"].lower():
            results.append({name: details})
        elif search_term.lower() in details["city"].lower():
            results.append({name: details})

    return results
```

---

## Recommended Folder Structure

```text
python-practice-projects/
├── README.md
├── budget_tracker.py
├── password_checker.py
└── contact_book.py
```

---

## General Tips

- Build one feature at a time.
- Test each function before creating the full menu.
- Use clear variable names.
- Keep the seed data at the top of each Python file.
- Use functions to keep your code organized.
- Return values from functions instead of only printing inside them.
```
