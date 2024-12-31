import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt

EXPENSES_FILE = "expenses.txt"


def add_expense_gui():
    def save_expense():
        category = category_entry.get().strip()
        try:
            amount = float(amount_entry.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a number.")
            return

        date = date_entry.get().strip()
        try:
            datetime.strptime(date, "%m-%d-%Y")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please enter date as MM-DD-YYYY.")
            return

        with open(EXPENSES_FILE, "a") as file:
            file.write(f"{category},{amount},{date}\n")
        messagebox.showinfo("Success", "Expense added successfully!")
        add_window.destroy()

    add_window = tk.Toplevel()
    add_window.title("Add Expense")

    tk.Label(add_window, text="Category:").grid(row=0, column=0, padx=10, pady=10)
    category_entry = tk.Entry(add_window)
    category_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Amount:").grid(row=1, column=0, padx=10, pady=10)
    amount_entry = tk.Entry(add_window)
    amount_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Date (MM-DD-YYYY):").grid(row=2, column=0, padx=10, pady=10)
    date_entry = tk.Entry(add_window)
    date_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Button(add_window, text="Save", command=save_expense).grid(row=3, column=0, columnspan=2, pady=20)


def view_expenses_gui():
    if not os.path.exists(EXPENSES_FILE):
        messagebox.showinfo("Info", "No expenses recorded yet.")
        return

    expenses = {}
    with open(EXPENSES_FILE, "r") as file:
        for line in file:
            category, amount, date = line.strip().split(",")
            if category not in expenses:
                expenses[category] = []
            expenses[category].append((float(amount), date))

    view_window = tk.Toplevel()
    view_window.title("View Expenses")

    row = 0
    for category, entries in expenses.items():
        tk.Label(view_window, text=f"{category}:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        row += 1
        if entries:
            for amount, date in entries:
                tk.Label(view_window, text=f"Amount: {amount} - Date: {date}").grid(row=row, column=0, padx=20, pady=2, sticky="w")
                row += 1
        else:
            tk.Label(view_window, text="No expenses recorded.").grid(row=row, column=0, padx=20, pady=2, sticky="w")
            row += 1


def monthly_summary_gui():
    if not os.path.exists(EXPENSES_FILE):
        messagebox.showinfo("Info", "No expenses recorded yet.")
        return

    year_month = simpledialog.askstring("Monthly Summary", "Enter month and year (MM-YYYY):")
    if not year_month:
        return

    try:
        datetime.strptime(year_month, "%m-%Y")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please enter month and year as MM-YYYY.")
        return

    expenses = {}
    total_expenses = 0

    with open(EXPENSES_FILE, "r") as file:
        for line in file:
            category, amount, date = line.strip().split(",")
            date_obj = datetime.strptime(date, "%m-%d-%Y")
            if date_obj.strftime("%m-%Y") == year_month:
                if category not in expenses:
                    expenses[category] = 0
                expenses[category] += float(amount)
                total_expenses += float(amount)

    if not expenses:
        messagebox.showinfo("Info", "No expenses recorded for the selected month.")
        return

    summary_window = tk.Toplevel()
    summary_window.title("Monthly Summary")

    tk.Label(summary_window, text=f"Monthly Summary ({datetime.strptime(year_month, '%m-%Y').strftime('%B %Y')}):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    tk.Label(summary_window, text=f"Total Expenses: {total_expenses}").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    tk.Label(summary_window, text="By Category:").grid(row=2, column=0, padx=10, pady=10, sticky="w")

    row = 3
    categories = []
    amounts = []
    for category, total in expenses.items():
        tk.Label(summary_window, text=f"{category}: {total}").grid(row=row, column=0, padx=20, pady=5, sticky="w")
        categories.append(category)
        amounts.append(total)
        row += 1

    def show_pie_chart():
        plt.figure(figsize=(6, 6))
        plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
        plt.title(f"Expense Distribution ({datetime.strptime(year_month, '%m-%Y').strftime('%B %Y')})")
        plt.show()

    tk.Button(summary_window, text="Show Pie Chart", command=show_pie_chart).grid(row=row, column=0, pady=20)


def main():
    root = tk.Tk()
    root.title("Personal Expense Tracker")

    tk.Button(root, text="Add Expense", command=add_expense_gui, width=20).pack(pady=10)
    tk.Button(root, text="View Expenses", command=view_expenses_gui, width=20).pack(pady=10)
    tk.Button(root, text="Monthly Summary", command=monthly_summary_gui, width=20).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
