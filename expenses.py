import json

def add_expense(expense_list):
    print(" ADD EXPENSE ")
    continue_adding = True
    
    while continue_adding:
        expense_name=input("enter your shopping type: ")
        amount=int(input("enter the amount : "))
    
        expense = {
                        "expense":expense_name,
                        "amount":amount,
                        }
        expense_list.append(expense)
        save_expenses(expense_list)
        x = input("Do you want to add another expense ?")
        if( x == "no"):
                        continue_adding = False
    total = 0
    for expense in expense_list:
                total = total + expense["amount"]
                print(expense["expense"])
                print(expense["amount"])
    print("Total : ", total)
    
def view_expense(expense_list):

    if expense_list != []:
        print("VIEW EXPENSE")

        total = 0

        for expense in expense_list:
            total = total + expense["amount"]
            print(expense["expense"])
            print(expense["amount"])

        print("Total :", total)

    else:
        print("No expenses found.")
        
def save_expenses(expense_list):
    
    file = open("data/expenses.json", "w")
    json.dump(expense_list, file)
    file.close()
    
def load_expenses():
    try:
        with open("data/expenses.json", "r") as file :
            expense_list = json.load(file)
            return expense_list
    except (json.decoder.JSONDecodeError , FileNotFoundError) :
        return[]
    
def display_numbered_expenses(expense_list):
    if  not expense_list:
        print("No expenses available.")
        return
    for index , expense in enumerate(expense_list):
        print(f"{index + 1}. {expense['expense']} : ₹{expense['amount']}")
        
def delete_expense(expense_list):
    if not expense_list:
        print("No expenses available.")
        return

    display_numbered_expenses(expense_list)
    while True:
        try:
            selected_expense = int(input("Select expense number to delete:  "))
            if selected_expense < 1 or selected_expense > len(expense_list):
                print(f"Please enter a number between 1 and {len(expense_list)}.")
                continue
            selected_index = selected_expense - 1
            expense_list.pop(selected_index)
            save_expenses(expense_list)
            print("Expense deleted successfully.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
    