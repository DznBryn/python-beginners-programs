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


def add_income(budget_data, amount):
    budget_data["income"] += amount


def add_expense(budget_data, name, category, amount):
    budget_data["expenses"].append({
        "name": name,
        "category": category,
        "amount": amount
    })


def get_total_expenses(budget_data):
    return sum(expense["amount"] for expense in budget_data["expenses"])


def get_remaining_balance(budget_data):
    total_expenses = get_total_expenses(budget_data)
    return budget_data["income"] - total_expenses


def get_expenses_by_category(budget_data, category):
    return [expense for expense in budget_data["expenses"] if expense["category"] == category]



def print_menu():
    print("\nPersonal Budget Tracker")
    print("1. Add income")
    print("2. Add expense")
    print("3. View all expenses")
    print("4. View total expenses")
    print("5. View spending by category")
    print("6. View remaining balance")
    print("7. Exit")

while True:
    print_menu()
    choice_input = input("Enter your choice: ").strip()

    if choice_input == "1":
        amount = float(input("Enter income amount: ").strip())
        add_income(budget_data, amount)
        print(f"Income updated. Current total income: ${budget_data['income']:.2f}")

    elif choice_input == "2":
        name = input("Enter expense name: ").strip()
        category = input("Enter expense category: ").strip()
        amount = float(input("Enter expense amount: ").strip())
        add_expense(budget_data, name, category, amount)
        print(f"Expense '{name}' added successfully!")

    elif choice_input == "3":
        if not budget_data["expenses"]:
            print("No expenses recorded.")
        else:
            print("Expenses:")
            for expense in budget_data["expenses"]:
                print(f"Name: {expense['name']}, Category: {expense['category']}, Amount: ${expense['amount']:.2f}")

    elif choice_input == "4":
        total_expenses = get_total_expenses(budget_data)
        print(f"Total expenses: ${total_expenses:.2f}")

    elif choice_input == "5":
        category = input("Enter category to view expenses: ").strip()
        expenses_by_category = get_expenses_by_category(budget_data, category)
        if not expenses_by_category:
            print(f"No expenses found in category '{category}'.")
        else:
            print(f"Expenses in category '{category}':")
            for expense in expenses_by_category:
                print(f"Name: {expense['name']}, Amount: ${expense['amount']:.2f}")

    elif choice_input == "6":
        remaining_balance = get_remaining_balance(budget_data)
        print(f"Remaining balance: ${remaining_balance:.2f}")

    elif choice_input == "7":
        print("Exiting Personal Budget Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
