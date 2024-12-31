# Personal Expense Tracker

## Overview
The Personal Expense Tracker is a Python-based application designed to help users manage their expenses efficiently. It provides features to add, view, and summarize expenses, as well as visualize expense distributions with pie charts. The application uses a graphical user interface (GUI) created with Tkinter and stores expense data persistently in a text file.

## Features
- **Add Expense**: Users can record expenses by specifying a category, amount, and date.
- **View Expenses**: View all recorded expenses categorized for better organization.
- **Monthly Summary**: Generate summaries of expenses for a specific month, including a breakdown by category and total expenses.
- **Pie Chart Visualization**: Visualize the distribution of expenses by category for a selected month.

## File Handling
Expense data is stored in a text file named `expenses.txt` in the following format:
```
Category,Amount,MM-DD-YYYY
```
Example:
```
Food,200,12-23-2024
Travel,150,12-25-2024
```

## Requirements
- Python 3.x
- Tkinter (comes pre-installed with Python)
- Matplotlib (install using `pip install matplotlib`)

## How to Run
1. Ensure you have Python installed on your system.
2. Install the required dependency:
   ```
   pip install matplotlib
   ```
3. Save the script as `expense_tracker.py`.
4. Run the script:
   ```
   python expense_tracker.py
   ```

## Usage
1. **Add Expense**:
   - Click "Add Expense" on the main menu.
   - Enter the category, amount, and date (in MM-DD-YYYY format).
   - Click "Save" to record the expense.

2. **View Expenses**:
   - Click "View Expenses" on the main menu.
   - View the recorded expenses categorized for better understanding.

3. **Monthly Summary**:
   - Click "Monthly Summary" on the main menu.
   - Enter the month and year (in MM-YYYY format) for the summary.
   - View the total expenses and expenses by category.
   - Optionally, click "Show Pie Chart" to visualize the distribution.

4. **Exit**:
   - Click "Exit" on the main menu to close the application.


## Future Improvements
- Add the ability to edit or delete existing expenses.
- Provide options to export summaries as CSV or PDF files.
- Enhance the UI for better usability.

## License
This project is licensed under the MIT License.

---
Feel free to contribute to the project by submitting issues or pull requests!

