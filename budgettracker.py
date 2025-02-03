#budgettracker
#a budget tracker app that stores the values into a json file
import json

def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense["amount"]
    return sum

def get_balance(budget,expenses):
    return budget - get_total_expenses(expenses)
    
def addtobudget(budget, plusamount):
    budget += plusamount 
    return budget
    
def remove_expense(expenses):
    for expense in expenses:
        print(f"- {expense['number']} - {expense['description']}: {expense['amount']}")
    try:
        number_to_remove = int(input("Enter the number of the expense to remove: "))
        # Find the expense with the specified number
        expense_to_remove = next((expense for expense in expenses if expense['number'] == number_to_remove), None)
        
        if expense_to_remove:
            expenses.remove(expense_to_remove)
            print(f"Removed expense {expense_to_remove['description']} with amount {expense_to_remove['amount']}")
            for index, expense in enumerate(expenses):
                expense['number'] = index + 1
        else:
            print("No expense found with that number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")    
       

def add_expense(expenses, description, amount):
    number = len(expenses) + 1
    expenses.append({"description": description, "amount": amount, "number": number })
    print(f"Added expense {number} - {description}, Amount: {amount}")
    
def show_budget_details(budget, expenses):
    print("*************************")
    print(f"Total budget: {budget}")
    print("***************************")
    for expense in expenses:
        print(f"- {expense['number']} - {expense['description']}: {expense['amount']}")
    print(f"Total spent: {get_total_expenses(expenses)}")
    print(f"Remaining budget: {get_balance(budget, expenses)}")
def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data ["initial_budget"], data ["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []
def save_budget_details(filepath, budget, expenses):
    data = {
        'initial_budget': budget,
        'expenses': expenses,
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    print("Welcome to the Budget tracking app")
    print("***************************************")
    #filepath = "PUT YOUR DESIRED FILEPATH HERE AND UNCOMENT THIS LINE"
    initial_budget, expenses = load_budget_data(filepath)    
    if initial_budget == 0:
        initial_budget = float(input("Give your initial budget to begin: "))
    budget = initial_budget
    
    while True:
        print("What would you like to do?")
        print("1. add expenses")
        print ("2. add money")
        print("3. show budget details")
        print("4. remove an expense")
        print("5. exit the app")
        choice = input("Enter your choice: ")
        
        
        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, description, amount)
        elif choice == "2":
            plusamount = float(input("How much are you adding?: "))
            budget = addtobudget(budget,plusamount)
        elif choice == "3":
            show_budget_details(budget,expenses)
        elif choice == "4":
            remove_expense(expenses)
        elif choice == "5":
            save_budget_details(filepath, budget, expenses)
            print("Ending program********")
            break
        else:
            print("Invalid choice, please pick a valid option")
            








if __name__ == "__main__":
    main()