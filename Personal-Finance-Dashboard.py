#Prompt user for input for weekly expenses
def get_weekly_expenses():
    weekly_expenses = dict() #Create new dict to store weekly expenses
    escape_code = 'n'
    user_input = ""
    expense_counter = 1
    print("*Weekly Expenses*")

    #Take input until user types escape code
    while user_input != escape_code:
        print(f"\n--Expense {expense_counter}--")
        print("Enter expense name: ", end="", flush = True)
        expense_name = input()
        print(expense_name)
        print("Enter expense amount: ", end="", flush = True)
        user_input = input()
        #Verify that input amount is a float
        try:
            expense_amount = float(user_input)
            print(f"${expense_amount:.2f}")
            weekly_expenses.update({expense_name:expense_amount})
        except:
            print("Invalid input")
        #Check if user wishes to add another expense
        print("Add another expense? (y/n) ", end="", flush = True) 
        user_input = input()
        expense_counter += 1

    #Return weekly expense dictionary
    return weekly_expenses


#Prompt user for input for monthly expenses
def get_monthly_expenses():
    monthly_expenses = dict() #Create new dict to store monthly expenses
    escape_code = 'n'
    user_input = ""
    expense_counter = 1
    print("*Monthly Expenses*")

    #Take input until user types escape code
    while user_input != escape_code:
        print(f"\n--Expense {expense_counter}--")
        print("Enter expense name: ", end="", flush = True)
        expense_name = input()
        print(expense_name)
        print("Enter expense amount: ", end="", flush = True)
        user_input = input()
        #Verify that input amount is a float
        try:
            expense_amount = float(user_input)
            print(f"${expense_amount:.2f}")
            monthly_expenses.update({expense_name:expense_amount})
        except:
            print("Invalid input")
        #Check if user wishes to add another expense
        print("Add another expense? (y/n) ", end="", flush = True) 
        user_input = input()
        expense_counter += 1

    #Return monthly expense dictionary
    return monthly_expenses

#Prompt user for input for annual expenses
def get_annual_expenses():
    annual_expenses = dict() #Create new dict to store annual expenses
    escape_code = 'n'
    user_input = ""
    expense_counter = 1
    print("*Annual Expenses*")

    #Take input until user types escape code
    while user_input != escape_code:
        print(f"\n--Expense {expense_counter}--")
        print("Enter expense name: ", end="", flush = True)
        expense_name = input()
        print(expense_name)
        print("Enter expense amount: ", end="", flush = True)
        user_input = input()
        #Verify that input amount is a float
        try:
            expense_amount = float(user_input)
            print(f"${expense_amount:.2f}")
            annual_expenses.update({expense_name:expense_amount})
        except:
            print("Invalid input")
        #Check if user wishes to add another expense
        print("Add another expense? (y/n) ", end="", flush = True) 
        user_input = input()
        expense_counter += 1

    #Return weekly expense dictionary
    return annual_expenses


if __name__ == "__main__":
    #Test weekly
    weekly_expenses = get_weekly_expenses()
    print("\n")
    print(weekly_expenses)

    #Test monthly
    monthly_expenses = get_monthly_expenses()
    print("\n")
    print(monthly_expenses)

    #Test annual
    annual_expenses = get_annual_expenses()
    print("\n")
    print(annual_expenses)