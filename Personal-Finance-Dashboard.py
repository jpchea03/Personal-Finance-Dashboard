# Imports
import csv
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# Function to save expenses to a CSV file
def save_expenses_to_csv(expenses, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write headers
        writer.writerow(["Expense Type", "Name", "Amount"])
        # Write each expense
        for expense_type, expense_dict in expenses.items():
            for name, amount in expense_dict.items():
                writer.writerow([expense_type, name, amount])
    print(f"Expenses saved to {filename}")

# Function to load expenses from a CSV file
def load_expenses_from_csv(filename):
    expenses = {"weekly": {}, "monthly": {}, "annual": {}}
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                expense_type, name, amount = row
                expenses[expense_type][name] = float(amount)
    except FileNotFoundError:
        print(f"{filename} not found. Returning empty expenses.")
    return expenses

# Prompt user for input for weekly expenses
def get_weekly_expenses():
    weekly_expenses = dict()  # Create new dict to store weekly expenses
    escape_code = 'n'
    user_input = ""
    expense_counter = 1
    print("\n*Weekly Expenses*")

    # Take input until user types escape code
    while user_input != escape_code:
        print(f"\n--Expense {expense_counter}--")
        print("Enter expense name: ", end="", flush=True)
        expense_name = input()
        print(expense_name)
        print("Enter expense amount: ", end="", flush=True)
        user_input = input()
        # Verify that input amount is a float
        try:
            expense_amount = float(user_input)
            print(f"${expense_amount:.2f}")
            weekly_expenses.update({expense_name: expense_amount})
        except:
            print("Invalid input")
        # Check if user wishes to add another expense
        print("Add another expense? (y/n) ", end="", flush=True)
        user_input = input()
        expense_counter += 1

    # Return weekly expense dictionary
    return weekly_expenses

# Prompt user for input for monthly expenses
def get_monthly_expenses():
    monthly_expenses = dict()  # Create new dict to store monthly expenses
    escape_code = 'n'
    user_input = ""
    expense_counter = 1
    print("\n*Monthly Expenses*")

    # Take input until user types escape code
    while user_input != escape_code:
        print(f"\n--Expense {expense_counter}--")
        print("Enter expense name: ", end="", flush=True)
        expense_name = input()
        print(expense_name)
        print("Enter expense amount: ", end="", flush=True)
        user_input = input()
        # Verify that input amount is a float
        try:
            expense_amount = float(user_input)
            print(f"${expense_amount:.2f}")
            monthly_expenses.update({expense_name: expense_amount})
        except:
            print("Invalid input")
        # Check if user wishes to add another expense
        print("Add another expense? (y/n) ", end="", flush=True)
        user_input = input()
        expense_counter += 1

    # Return monthly expense dictionary
    return monthly_expenses

# Prompt user for input for annual expenses
def get_annual_expenses():
    annual_expenses = dict()  # Create new dict to store annual expenses
    escape_code = 'n'
    user_input = ""
    expense_counter = 1
    print("\n*Annual Expenses*")

    # Take input until user types escape code
    while user_input != escape_code:
        print(f"\n--Expense {expense_counter}--")
        print("Enter expense name: ", end="", flush=True)
        expense_name = input()
        print(expense_name)
        print("Enter expense amount: ", end="", flush=True)
        user_input = input()
        # Verify that input amount is a float
        try:
            expense_amount = float(user_input)
            print(f"${expense_amount:.2f}")
            annual_expenses.update({expense_name: expense_amount})
        except:
            print("Invalid input")
        # Check if user wishes to add another expense
        print("Add another expense? (y/n) ", end="", flush=True)
        user_input = input()
        expense_counter += 1

    # Return annual expense dictionary
    return annual_expenses

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Home")
        self.setGeometry(400, 400, 1000, 600)

        l1 = QLabel("Personal Finance Dashboard")

        layout = QVBoxLayout()
        layout.addWidget(l1)
        self.setLayout(layout)

        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
