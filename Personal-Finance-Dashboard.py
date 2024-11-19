import csv

global weekly_expenses
global monthly_expenses
global annual_expenses

global monthlyAllowance
global monthlySavings
global monthlyNecessaryExpenses

global userInfoArray
global annualIncome
global currentSavings
global userName
global userState
global userJobTitle

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


# Unified function to prompt user for expenses based on type
def set_expenses(expense_type):
    expenses = dict()  # Create a new dict to store expenses of the given type
    escape_code = 'n'
    user_input = ""
    expense_counter = 1
    print(f"\n*{expense_type.capitalize()} Expenses*")

    # Take input until user types escape code
    while user_input != escape_code:
        print(f"\n--Expense {expense_counter}--")
        expense_name = input("Enter expense name: ")
        user_input = input("Enter expense amount: ")
        # Verify that input amount is a float
        try:
            expense_amount = float(user_input)
            expenses[expense_name] = expense_amount
            print(f"Added {expense_name} with amount ${expense_amount:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number for the expense amount.")
        
        # Check if user wishes to add another expense
        user_input = input("Add another expense? (y/n): ").lower()
        expense_counter += 1
    return expenses

##================================================================

def saveUserInfo(user_info, filename="userInfo.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write headers
        writer.writerow(["annualIncome", "currentSavings", "userName", "userState", "userJobTitle"])
        # Write user information (array format)
        writer.writerow(user_info)
    print(f"User information saved to {filename}")

# Function to load user information from a CSV file
def loadUserInfo(filename="userInfo.csv"):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            user_info = next(reader)  # Read the first data row
    except StopIteration:
        print(f"{filename} is empty. Returning default user information.")
        user_info = [0.0, 0.0, "", "", ""]  # Default values
    return user_info




#==========buttons==========

def changeUserInfoButton():
    annualIncome = input("\nAnnual Income: ")
    currentSavings = input("Current Savings: ")
    userName = input("Name: ")
    userState = input("State: ")
    userJobTitle = input("Job Title: ")
    userInfoArray = [annualIncome,currentSavings, userName, userState, userJobTitle]
    #print(userInfoArray)
    return userInfoArray
def addWeeklyExpensesButton():
    weekly_expenses = set_expenses("weekly")
    return
def addMonthlyExpensesButton():
    monthly_expenses = set_expenses("monthly")
    return
def addAnnualExpensesButton():
    annual_expenses = set_expenses("annual")
    return
def showVisualizationButton():
    return
def makeFinancialSuggestionButton():
    return
def printInfo():
    print("\nLoaded expenses:")
    #print(load_expenses_from_csv('expenses.csv'))
    print(userInfoArray)
    #print(userName)
    print(weekly_expenses, monthly_expenses, annual_expenses)
    return



if __name__ == "__main__":
   
    weekly_expenses, monthly_expenses, annual_expenses = load_expenses_from_csv('expenses.csv').values()
    userInfoArray = loadUserInfo()
    

    while True:
        print("\nTHIS IS THE CURRENT UI HOME PAGE. PLEASE SELECT A BUTTON\n-----------------------------")
        print("Change User Info: U")
        print("Add Weekly Expenses: W")
        print("Add Monthly Expenses: M")
        print("Add Annual Expenses: A")
        #print("Show Visualization: V")
        #print("Make Suggestion: S")
        #print("Quit Program: Q")
        print("Print Info: P")
        user_input = input("\nUser Input: ").lower()
        if user_input=='u':
            userInfoArray = changeUserInfoButton()
        elif user_input=='w':
            addWeeklyExpensesButton()
        elif user_input=='m':
            addMonthlyExpensesButton()
        elif user_input=='a':
            addAnnualExpensesButton()
        elif user_input=='v':
            showVisualizationButton()
        elif user_input=='s':
            makeFinancialSuggestionButton()
        elif user_input=='p':
            printInfo()
        else: break
    



    # save user info to csv
    saveUserInfo(userInfoArray)

    # Combine all expenses into a single dictionary and saves to csv file
    all_expenses = {
        "weekly": weekly_expenses,
        "monthly": monthly_expenses,
        "annual": annual_expenses
    }
    save_expenses_to_csv(all_expenses, 'expenses.csv')
    



