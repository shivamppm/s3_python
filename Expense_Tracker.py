import os
from datetime import datetime

EXPENSES_FILE = "expenses.txt"


def add_expense():
    category = input("Enter category (e.g., Food, Travel): ").strip()
    try:
        amount = float(input("Enter amount: ").strip())
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    date = input("Enter date (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please enter date as YYYY-MM-DD.")
        return

    with open(EXPENSES_FILE, "a") as file:
        file.write(f"{category},{amount},{date}\n")
    print("Expense added successfully! (Expense recorded in expenses.txt)")


def view_expenses():
    if not os.path.exists(EXPENSES_FILE):
        print("No expenses recorded yet.")
        return

    expenses = {}
    with open(EXPENSES_FILE, "r") as file:
        for line in file:
            category, amount, date = line.strip().split(",")
            if category not in expenses:
                expenses[category] = []
            expenses[category].append((float(amount), date))

    print("Expenses:")
    for category, entries in expenses.items():
        print(f"{category}:")
        if entries:
            for i, (amount, date) in enumerate(entries, start=1):
                print(f"{i}. Amount: {amount} - Date: {date}")
        else:
            print("No expenses recorded.")


def monthly_summary():
    if not os.path.exists(EXPENSES_FILE):
        print("No expenses recorded yet.")
        return

    year_month = input("Enter month and year (YYYY-MM): ").strip()
    try:
        datetime.strptime(year_month, "%Y-%m")
    except ValueError:
        print("Invalid date format. Please enter month and year as YYYY-MM.")
        return

    expenses = {}
    total_expenses = 0

    with open(EXPENSES_FILE, "r") as file:
        for line in file:
            category, amount, date = line.strip().split(",")
            if date.startswith(year_month):
                if category not in expenses:
                    expenses[category] = 0
                expenses[category] += float(amount)
                total_expenses += float(amount)

    print(f"Monthly Summary ({datetime.strptime(year_month, '%Y-%m').strftime('%B %Y')}):")
    print(f"Total Expenses: {total_expenses}")
    print("By Category:")
    for category, total in expenses.items():
        print(f"{category}: {total}")


def main():
    while True:
        print("\nWelcome to Personal Expense Tracker!")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
