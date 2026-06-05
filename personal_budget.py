print(input("""Personal Budget Tracker
1. Add income
2. Add expense
3. View all expenses
4. View total expenses
5. View spending by category
6. View remaining balance
7. Exit
Please select an option (1-7): """))

if input == "1":
    def add_income(budget_data, amount):
        budget_data = {
            "income": 0,
            "expenses": []
        }
        budget_data["income"] += amount
        print(f"Income of ${amount} added.")

       
