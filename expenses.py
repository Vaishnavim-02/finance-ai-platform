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
    if not expense_list:
        print("No expenses available.")
        return
    print("VIEW EXPENSE")
    display_expenses(expense_list)
    total = calculate_total(expense_list)
    print("Total:", total)

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
    
def edit_category(expense):
    while True:
        new_expense = input("Enter new expense :  ")
        new_expense = new_expense.strip()
        if not new_expense:
            print("Expense name cannot be empty. \n Please try again ")
            continue
        
        expense["expense"] = new_expense
        break


def edit_amount(expense):
    while True:
        try:
            new_amount = float(input("Enter new amount : "))
            if(new_amount > 0 ):
                expense["amount"] = new_amount
                break
            else:
                print(" Please enter a valid amount.")
        except ValueError:
            print(" Invalid Amount. \n Please try again")
            continue
            
def edit_expense(expense_list):
    if not expense_list:
            print("No expenses available.")
            return
    display_numbered_expenses(expense_list)
    while True:
                try:
                    expense_number = int(input("Select expense number to edit:  "))
                    if  expense_number < 1 or expense_number > len(expense_list):
                        print(f"Please enter a number between 1 and {len(expense_list)}.")
                        continue
                    selected_index = expense_number - 1
                    selected_expense = expense_list[selected_index]
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue
    while True:
        edit_choice =input("Enter your choice you would like to edit ( 1-3) ?")
                
        if edit_choice== "1":
            edit_category(selected_expense)
            break
        
        elif edit_choice== "2":
            edit_amount(selected_expense)
            break
        
        elif edit_choice== "3":
            edit_category(selected_expense)
            edit_amount(selected_expense)
            break
        
        else:
            print("Invalid choice ")
            continue
    save_expenses(expense_list)
    print("Expense updated successfully !")
        
def search_expense(expense_list):
    if not expense_list:
                print("No expenses match available.")
                return
    search = input("enter the expense you want to search ?")
    print(search)
    
    if search == True:
        total = 0
        total = total + expense["amount"]
        print("Total :", total)
        print("Search Found")
    else:
        print("No Match Found")
        
def display_expenses(expense_list):
    if not expense_list:
        print("No expenses available.")
        return
            
    for expense in expense_list:
            print(expense["expense"])
            print(expense["amount"])
    
def calculate_total(expense_list):
    total = 0
    for expense in expense_list:
        total = total + expense["amount"]
    return total

def search_expense(expense_list):
    if not expense_list :
        print("No expenses available")
        return
    search = input("Enter the expense you want to search ?").strip().lower()
    
    matching_expenses = []
    for expense in expense_list:
        expense_name = expense["expense"].strip().lower()

        if search in expense_name:
            matching_expenses.append(expense)
        
    if not matching_expenses:
        print("No matching expense found.")
        return
    
    view_expense(matching_expenses)
def category_summary(expense_list):
    if not expense_list:
        print("No expenses available.")
        return
    print("CATEGORY SUMMARY")
    print("-" * 20)
    
    category_summary = {}
    for expense in expense_list:
        category = expense["expense"]
        amount = expense["amount"]
        
        if category in category_summary:
            category_summary[category] = category_summary[category] + amount
        else:
            category_summary[category] = amount
            
    for category, total in category_summary.items():
                print(category,":",total)
            
def highest_expense(expense_list):
    if not expense_list:
        print("No Expenses Available")
        return
    
    highest_expense = expense_list[0]
    
    for expense in expense_list[1:]:
        if expense["amount"] > highest_expense["amount"]:
            highest_expense = expense
        
    print("=" * 35)
    print("      Highest Expense")
    print("=" * 35)
    print(f"Expense  : {highest_expense['expense']}")
    print(f"Category : {highest_expense['category']}")
    print(f"Amount   : ₹{highest_expense['amount']}")
    print("=" * 35)
            
    
        