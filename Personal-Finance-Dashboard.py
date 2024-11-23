# Imports
import csv
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import (
    QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QWidget, QLineEdit, QListWidget, QFormLayout, QMessageBox
)

class ExpenseWindow(QWidget):
    def __init__(self, title):
        super().__init__()
        self.expense_type = title.lower()  # "Weekly", "Monthly", etc.
        self.csv_filename = f"{self.expense_type}_expenses.csv"
        self.expenses = load_expenses_from_csv(self.csv_filename).get(self.expense_type, {})


        # Main layout for the window
        main_layout = QHBoxLayout()

        # Layout for adding expenses (left side)
        add_expense_layout = QVBoxLayout()
        add_expense_label = QLabel(f"Add {title} Expense")
        add_expense_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        add_expense_layout.addWidget(add_expense_label)

        # Fields for expense name and amount
        self.expense_name_input = QLineEdit()
        self.expense_name_input.setPlaceholderText("Expense Name")
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Amount")

        add_expense_layout.addWidget(self.expense_name_input)
        add_expense_layout.addWidget(self.amount_input)

        # Button to add the expense
        add_expense_btn = QPushButton("Add Expense")
        add_expense_btn.clicked.connect(self.add_expense)
        add_expense_layout.addWidget(add_expense_btn)

        # Layout for listing expenses (right side)
        expenses_list_layout = QVBoxLayout()
        expenses_list_label = QLabel(f"{title} Expenses")
        expenses_list_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        expenses_list_layout.addWidget(expenses_list_label)

        self.expenses_list = QListWidget()
        expenses_list_layout.addWidget(self.expenses_list)
        self.populate_expense_list()

        # Buttons for managing expenses
        manage_expenses_layout = QHBoxLayout()
        
        save_expenses_btn = QPushButton("Save Expenses to CSV")
        save_expenses_btn.clicked.connect(self.save_expenses_to_csv)
        manage_expenses_layout.addWidget(save_expenses_btn)

        delete_expense_btn = QPushButton("Delete Selected Expense")
        delete_expense_btn.clicked.connect(self.delete_selected_expense)
        manage_expenses_layout.addWidget(delete_expense_btn)

        expenses_list_layout.addLayout(manage_expenses_layout)

        # Add both layouts to the main layout
        main_layout.addLayout(add_expense_layout)
        main_layout.addLayout(expenses_list_layout)

        self.setLayout(main_layout)
        self.setWindowTitle(f"Add {title} Expenses")
        self.setGeometry(200, 200, 500, 300)

    def add_expense(self):
        """Add a new expense to the list and internal dictionary."""
        expense_name = self.expense_name_input.text()
        amount = self.amount_input.text()

        if not expense_name or not amount:
            QMessageBox.warning(self, "Input Error", "Please enter expense name.")
            return
        if not amount:
            QMessageBox.warning(self, "Input Error","Please enter expense amount.")

        try:
            amount = float(amount)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Amount must be a number!")
            return

        self.expenses[expense_name] = amount
        self.expenses_list.addItem(f"{expense_name}: ${amount:.2f}")
        self.expense_name_input.clear()
        self.amount_input.clear()
        self.save_expenses_to_csv()

    def populate_expense_list(self):
        """Populate the list widget with existing expenses."""
        self.expenses_list.clear()
        for name, amount in self.expenses.items():
            self.expenses_list.addItem(f"{name}: ${amount:.2f}")

    def save_expenses_to_csv(self):
        """Save the expenses to the CSV file."""
        try:
            with open(self.csv_filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Expense Type", "Name", "Amount"])
                for name, amount in self.expenses.items():
                    writer.writerow([self.expense_type, name, amount])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save expenses: {e}")

    def delete_selected_expense(self):
        """Delete the selected expense from the list and CSV."""
        selected_item = self.expenses_list.currentItem()
        if selected_item:
            # Extract the expense name from the selected item
            expense_text = selected_item.text()
            expense_name = expense_text.split(":")[0]

            # Remove from internal dictionary and GUI
            if expense_name in self.expenses:
                del self.expenses[expense_name]
                self.populate_expense_list()  # Refresh the list
                self.save_expenses_to_csv()

                QMessageBox.information(self, "Success", f"Expense '{expense_name}' deleted.")
            else:
                QMessageBox.warning(self, "Error", f"Expense '{expense_name}' not found!")
        else:
            QMessageBox.warning(self, "Selection Error", "No expense selected for deletion.")

class VisualizationMenuWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Main layout for the window
        layout = QVBoxLayout()

        # Header label
        header_label = QLabel("Choose a Visualization")
        header_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(header_label)

        # Buttons for visualizations
        weekly_vis_btn = QPushButton("Weekly Expenses")
        weekly_vis_btn.clicked.connect(self.show_weekly_expenses_chart)
        layout.addWidget(weekly_vis_btn)

        monthly_vis_btn = QPushButton("Monthly Expenses")
        monthly_vis_btn.clicked.connect(self.show_monthly_expenses_chart)
        layout.addWidget(monthly_vis_btn)

        yearly_vis_btn = QPushButton("Yearly Expenses")
        yearly_vis_btn.clicked.connect(self.show_yearly_expenses_chart)
        layout.addWidget(yearly_vis_btn)

        self.setLayout(layout)
        self.setWindowTitle("Visualization Menu")
        self.setGeometry(250, 250, 300, 200)

    def load_expenses_from_csv(self, filename):
        """Helper function to load expenses from a CSV file."""
        expenses = {}
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    _, name, amount = row  # Ignore the first column (Expense Type)
                    expenses[name] = float(amount)
        except FileNotFoundError:
            print(f"{filename} not found. Returning empty data.")
        except ValueError:
            print(f"Invalid data format in {filename}. Skipping malformed rows.")
        return expenses

    
    def show_weekly_expenses_chart(self):
        """Show a bar chart for weekly expenses."""
        weekly_expenses = self.load_expenses_from_csv("weekly_expenses.csv")
        names = list(weekly_expenses.keys())
        amounts = list(weekly_expenses.values())

        plt.bar(names, amounts, color="skyblue")
        plt.title("Weekly Expenses")
        plt.xlabel("Expense Name")
        plt.ylabel("Amount ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


    def show_monthly_expenses_chart(self):
        """Show a bar chart for monthly expenses."""
        monthly_expenses = self.load_expenses_from_csv("monthly_expenses.csv")
        names = list(monthly_expenses.keys())
        amounts = list(monthly_expenses.values())

        plt.bar(names, amounts, color="lightgreen")
        plt.title("Monthly Expenses")
        plt.xlabel("Expense Name")
        plt.ylabel("Amount ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def show_yearly_expenses_chart(self):
        """Show a bar chart for yearly expenses."""
        yearly_expenses = self.load_expenses_from_csv("annual_expenses.csv")
        names = list(yearly_expenses.keys())
        amounts = list(yearly_expenses.values())

        plt.bar(names, amounts, color="orange")
        plt.title("Yearly Expenses")
        plt.xlabel("Expense Name")
        plt.ylabel("Amount ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

class UpdateUserInfoWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Main layout for the window
        layout = QVBoxLayout()

        # Header label
        header_label = QLabel("Update User Information")
        header_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(header_label)

        # Form layout for user information fields
        form_layout = QFormLayout()

        # Fields for user information
        self.name_input = QLineEdit()
        self.annual_income_input = QLineEdit()
        self.current_funds_input = QLineEdit()
        self.state_input = QLineEdit()

        # Adding fields to the form
        form_layout.addRow("Name:", self.name_input)
        form_layout.addRow("Annual Income:", self.annual_income_input)
        form_layout.addRow("Current Funds:", self.current_funds_input)
        form_layout.addRow("State:", self.state_input)

        # Add form layout to the main layout
        layout.addLayout(form_layout)

        # Save button
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_user_info)
        layout.addWidget(save_button)

        # Set the main layout for the window
        self.setLayout(layout)
        self.setWindowTitle("Update User Info")
        self.setGeometry(300, 300, 400, 250)

    def save_user_info(self):
        # Collect the data from input fields
        name = self.name_input.text()
        annual_income = self.annual_income_input.text()
        current_funds = self.current_funds_input.text()
        state = self.state_input.text()

        # Placeholder functionality for saving data
        print("User Info Updated:")
        print(f"Name: {name}")
        print(f"Annual Income: {annual_income}")
        print(f"Current Funds: {current_funds}")
        print(f"State: {state}")

class PersonalFinanceDashboard(QWidget):
    def __init__(self):
        super().__init__()

        # Main layout
        main_layout = QVBoxLayout()

        # Header label
        header_label = QLabel("Personal Finance Dashboard")
        header_label.setStyleSheet("font-size: 24px; font-weight: bold; text-decoration: underline;")
        main_layout.addWidget(header_label)

        # Horizontal layout for user info and functions
        horizontal_layout = QHBoxLayout()

        # User Info layout
        user_info_layout = QVBoxLayout()
        user_info_label = QLabel("User Info")
        user_info_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        user_info_layout.addWidget(user_info_label)

        # Adding labels for User Info
        user_info_layout.addWidget(QLabel("Name: "))
        user_info_layout.addWidget(QLabel("Annual Income: "))
        user_info_layout.addWidget(QLabel("Current Funds: "))
        user_info_layout.addWidget(QLabel("State: "))

        # Functions layout
        functions_layout = QVBoxLayout()
        functions_label = QLabel("Functions")
        functions_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        functions_layout.addWidget(functions_label)

        # Add Weekly Expenses button
        add_weekly_expenses_btn = QPushButton("Add Weekly Expenses")
        add_weekly_expenses_btn.clicked.connect(self.open_weekly_expenses_window)
        functions_layout.addWidget(add_weekly_expenses_btn)

        # Add Monthly Expenses button
        add_monthly_expenses_btn = QPushButton("Add Monthly Expenses")
        add_monthly_expenses_btn.clicked.connect(self.open_monthly_expenses_window)
        functions_layout.addWidget(add_monthly_expenses_btn)

        # Add Annual Expenses button
        add_annual_expenses_btn = QPushButton("Add Annual Expenses")
        add_annual_expenses_btn.clicked.connect(self.open_annual_expenses_window)
        functions_layout.addWidget(add_annual_expenses_btn)

        # Visualization button
        visualization_btn = QPushButton("Visualization")
        visualization_btn.clicked.connect(self.open_visualization_menu)
        functions_layout.addWidget(visualization_btn)

        # Update User Info button
        update_user_info_btn = QPushButton("Update User Info")
        update_user_info_btn.clicked.connect(self.open_update_user_info_window)
        functions_layout.addWidget(update_user_info_btn)

        # Adding other buttons
        functions_layout.addWidget(QPushButton("Budget Suggestions"))

        # Adding user info and functions to the horizontal layout
        horizontal_layout.addLayout(user_info_layout)
        horizontal_layout.addLayout(functions_layout)

        # Adding everything to the main layout
        main_layout.addLayout(horizontal_layout)
        self.setLayout(main_layout)

        # Window settings
        self.setWindowTitle("Personal Finance Dashboard")
        self.setGeometry(100, 100, 600, 400)

    def open_weekly_expenses_window(self):
        self.weekly_expenses_window = ExpenseWindow("Weekly")
        self.weekly_expenses_window.show()

    def open_monthly_expenses_window(self):
        self.monthly_expenses_window = ExpenseWindow("Monthly")
        self.monthly_expenses_window.show()

    def open_annual_expenses_window(self):
        self.annual_expenses_window = ExpenseWindow("Annual")
        self.annual_expenses_window.show()


    def open_visualization_menu(self):
        # Create and show the VisualizationMenuWindow
        self.visualization_menu_window = VisualizationMenuWindow()
        self.visualization_menu_window.show()

    def open_update_user_info_window(self):
        self.update_user_info_window = UpdateUserInfoWindow()
        self.update_user_info_window.show()

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

if __name__ == "__main__":
    app = QApplication([])
    window = PersonalFinanceDashboard()
    window.show()
    app.exec()