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

# Get total expenses by summing the amounts of all expenses in the budget data.
def get_total_expenses(budget_data):
    return sum(expense["amount"] for expense in budget_data["expenses"])

# Calculate remaining balance by subtracting total expenses from total income.
def get_remaining_balance(budget_data):
    total_expenses = get_total_expenses(budget_data)
    return budget_data["income"] - total_expenses

# Get expenses by category by filtering the expenses list for those that match the specified category.
def get_expenses_by_category(budget_data, category):
    return [expense for expense in budget_data["expenses"] if expense["category"] == category]


# The following code provides a simple command-line interface for the personal budget tracker, allowing users to interact with the budget data and perform various operations such as adding income, adding expenses, viewing expenses, and calculating totals and remaining balance.
def print_menu():
    print("\nPersonal Budget Tracker")
    print("1. Add income")
    print("2. Add expense")
    print("3. View all expenses")
    print("4. View total expenses")
    print("5. View spending by category")
    print("6. View remaining balance")
    print("7. Exit")

# Main loop to display the menu and handle user choices for the personal budget tracker application.
while True:
    print_menu()
    choice_input = input("Enter your choice: ").strip()
# Handle user choices for adding income, adding expenses, viewing expenses, and calculating totals and remaining balance based on the user's input.
    if choice_input == "1":
        amount = float(input("Enter income amount: ").strip())
        add_income(budget_data, amount)
        print(f"Income updated. Current total income: ${budget_data['income']:.2f}")
# Handle adding a new expense by prompting the user for the expense name, category, and amount, and then calling the add_expense function to update the budget data with the new expense.
    elif choice_input == "2":
        name = input("Enter expense name: ").strip()
        category = input("Enter expense category: ").strip()
        amount = float(input("Enter expense amount: ").strip())
        add_expense(budget_data, name, category, amount)
        print(f"Expense '{name}' added successfully!")
# Handle viewing all expenses by iterating through the expenses list in the budget data and displaying each expense's name, category, and amount to the user.
    elif choice_input == "3":
        if not budget_data["expenses"]:
            print("No expenses recorded.")
        else:
            print("Expenses:")
            for expense in budget_data["expenses"]:
                print(f"Name: {expense['name']}, Category: {expense['category']}, Amount: ${expense['amount']:.2f}")
# Handle viewing total expenses by calling the get_total_expenses function and displaying the result to the user.
    elif choice_input == "4":
        total_expenses = get_total_expenses(budget_data)
        print(f"Total expenses: ${total_expenses:.2f}")
# Handle viewing expenses by category by prompting the user for a category and displaying the expenses that belong to that category.
    elif choice_input == "5":
        category = input("Enter category to view expenses: ").strip()
        expenses_by_category = get_expenses_by_category(budget_data, category)
        if not expenses_by_category:
            print(f"No expenses found in category '{category}'.")
        else:
            print(f"Expenses in category '{category}':")
            for expense in expenses_by_category:
                print(f"Name: {expense['name']}, Amount: ${expense['amount']:.2f}")
# Calculate and display the remaining balance by calling the get_remaining_balance function and showing the result to the user.
    elif choice_input == "6":
        remaining_balance = get_remaining_balance(budget_data)
        print(f"Remaining balance: ${remaining_balance:.2f}")
# Handle exit choice by breaking the loop and ending the program when the user selects the option to exit.
    elif choice_input == "7":
        print("Exiting Personal Budget Tracker. Goodbye!")
        break
# Handle invalid choices by prompting the user to enter a valid option from the menu.
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
