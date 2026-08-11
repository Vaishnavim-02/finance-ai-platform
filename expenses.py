import json

def add_expense(expense_list):
    print(" ADD EXPENSE ")
    continue_adding = True
    
    while continue_adding:
        expense_name=input("Enter Expense Name: ").strip().title()
        category=input("Enter Category Name : ").strip().title()
        amount=int(input("Enter The Amount : "))
    
        expense = {
                        "expense":expense_name,
                        "category":category,
                        "amount":amount,
                        }
        expense_list.append(expense)
        save_expenses(expense_list)
        x = input("Do you want to add another expense ?")
        if( x == "no"):
                        continue_adding = False
    view_expense(expense_list)
    
def view_expense(expense_list):
    if not expense_list:
        print("No expenses available.")
        return
    print("VIEW EXPENSE")
    display_expenses(expense_list)
    total = calculate_total(expense_list)
    print("Total:", total)

def save_expenses(expense_list):
    with open("data/expenses.json", "w") as file:
        json.dump(expense_list, file)

def load_expenses():
    try:
        with open("data/expenses.json", "r") as file :
            expense_list = json.load(file)
            return expense_list
    except (json.decoder.JSONDecodeError , FileNotFoundError) :
        return[]
    
def display_numbered_expenses(expense_list):
    for index , expense in enumerate(expense_list):
        print(f"{index + 1}. {expense['expense']} : ₹{expense['amount']}")
    
def select_expense(expense_list):
    display_numbered_expenses(expense_list)
    try:
        expense_number = int(input("Enter expense number: "))
    except ValueError:
        print("Please enter a valid number.")
        return None
    if expense_number < 1 or expense_number > len(expense_list):
        print("Invalid expense number.")
        return None
    return expense_number - 1

def delete_expense(expense_list):
    if not expense_list:
        print("No expenses available.")
        return
    index = select_expense(expense_list)
    if index is None:
        return
    deleted_expense = expense_list.pop(index)
    save_expenses(expense_list)
    print(f"'{deleted_expense['expense']}' deleted successfully.")

def edit_expense_name(expense):
    while True:
        new_expense = input("Enter new expense name: ").strip().title()
        if not new_expense:
            print("Expense name cannot be empty.")
            continue
        expense["expense"] = new_expense
        break

def edit_amount(expense):
    while True:
        try:
            new_amount = float(input("Enter new amount: "))
            if new_amount < 0:
                print("Amount cannot be negative.")
                continue
            expense["amount"] = new_amount
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            
def edit_expense(expense_list):
    if not expense_list:
        print("No expenses available.")
        return
    index = select_expense(expense_list)
    if index is None:
        return
    expense = expense_list[index]
    while True:
        print("=" * 35)
        print("EDIT EXPENSE")
        print("=" * 35)
        print("1. Edit Expense Name")
        print("2. Edit Category")
        print("3. Edit Amount")
        print("4. Back")
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        if choice == 1:
                edit_expense_name(expense)
                save_expenses(expense_list)
                print("Expense name updated successfully.")
        elif choice == 2:
            edit_expense_name(expense)
            save_expenses(expense_list)
            print("Category updated successfully.")
        elif choice == 3:
            edit_amount(expense)
            save_expenses(expense_list)
            print("Amount updated successfully.")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please choose between 1 and 4.")

def display_expenses(expense_list):
    for expense in expense_list:
            print(expense["expense"])
            print(expense["amount"])
            print(expense["category"])
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
    display_expenses(matching_expenses)

def category_summary(expense_list):
    if not expense_list:
        print("No expenses available.")
        return
    print("CATEGORY SUMMARY")
    print("-" * 20)
    
    category_summary = {}
    for expense in expense_list:
        category = expense["category"]
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
    
def lowest_expense(expense_list):
    if not expense_list:
        print("No Expenses Available")
        return
    
    lowest_expense= expense_list[0]
    
    for expense in expense_list[1:]:
        if expense["amount"] < lowest_expense["amount"]:
            lowest_expense = expense
        
    print("=" * 35)
    print("      Lowest Expense")
    print("=" * 35)
    print(f"Expense  : {lowest_expense['expense']}")
    print(f"Category : {lowest_expense['category']}")
    print(f"Amount   : ₹{lowest_expense['amount']}")
    print("=" * 35)
    
def average_expense(expense_list):
    if not expense_list:
        print("No expense Available")
        return
    total = 0
    Number_of_expenses = len(expense_list)
    for expense in expense_list:
        total += expense["amount"]
    average = total / Number_of_expenses
    print("=" * 35)
    print("      Average Expense")
    print("=" * 35)
    print(f"Average : ₹{average:.2f}")
    print("=" * 35)
    
def total_number_of_expenses(expense_list):
    number_of_expenses = len(expense_list)
    print("=" * 35)
    print("      Total Number of Expense")
    print("=" * 35)
    print(f"Total Expenses : {number_of_expenses}")
    print("=" * 35)
    
def expense_percentage(expense_list):
    if not expense_list:
        print("No Expense Available")
        return
    
    category_totals = {}
    total = 0
    for expense in expense_list:
        total += expense["amount"]
        category = expense["category"]
        amount = expense["amount"]
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
        
    print("=" * 35)
    print("      Expense Percentage ")
    print("=" * 35)
    
    for category, category_total in category_totals.items():
        percentage = (category_total / total) * 100
        print(f"{category:<15} : {percentage:.2f}%")
    print("=" * 35)
    
def sort_expenses(expense_list):
    if not expense_list:
        print("No Expense Available")
        return
    while True:
        print("=" * 35)
        print("SORT EXPENSE")
        print("=" * 35)
        print("1. Amount (Ascending)")
        print("2. Amount (Descending)")
        print("3. Expense Name (A-Z)")
        print("4. Expense Name (Z-A)")
        print("5. Category")
        print("6. Exit")
    
        try :
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue
        key = None
        reverse = False
        if choice == 1:
                key = lambda expense: expense["amount"]
        elif choice == 2:
                key =  lambda expense: expense["amount"]
                reverse = True
        elif choice == 3:
                key = lambda expense: expense["expense"]
        elif choice == 4:
                key = lambda expense: expense["expense"]
                reverse = True
        elif choice == 5:
                key = lambda expense: expense["category"]
        elif choice == 6:
                break
        else:
                print("Invalid Choice")
                continue
        sorted_expenses = sorted(
                                expense_list,
                                key=key,
                                reverse=reverse
                            )
        view_expense(sorted_expenses)
        break
    
def filter_expenses(expense_list):
    if not expense_list:
        print("No Expense Available")
        return

    while True:
        print("=" * 35)
        print("FILTER EXPENSE")
        print("=" * 35)
        print("1. Filter by Category")
        print("2. Filter by Amount (Greater than)")
        print("3. Filter by Amount (Less than)")
        print("4. Filter by Amount Range")
        print("5. Back")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == 1:

            categories = set()
            for expense in expense_list:
                categories.add(expense["category"])
            sorted_categories = sorted(categories)

            print("\nAvailable Categories:")
            for index, category in enumerate(sorted_categories, start=1):
                print(f"{index}. {category}")

            try:
                category_choice = int(input("Select a category: "))

                if category_choice < 1 or category_choice > len(sorted_categories):
                    print("Invalid category choice.")
                    continue

            except ValueError:
                print("Please enter a valid number.")
                continue

            selected_category = sorted_categories[category_choice - 1]
            filtered_expenses = filter_expenses_by_condition(
                expense_list,
                lambda expense: expense["category"] == selected_category
                )

            view_expense(filtered_expenses)
            break

        elif choice == 2:
            try:
                minimum_amount = int(input("Enter the amount : "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            filtered_expenses = filter_expenses_by_condition(
                expense_list,
                lambda expense: expense["amount"] > minimum_amount
                )
            if not filtered_expenses:
                    print("No Expense Found !")
                    continue
            view_expense(filtered_expenses)
            break

        elif choice == 3:
            try:
                maximum_amount = int(input("Enter the amount : "))
            except ValueError:
                print("Invalid input . Please enter a valid number.")
                continue
            filtered_expenses = filter_expenses_by_condition(
                expense_list,
                lambda expense: expense["amount"] < maximum_amount
                )
            if not filtered_expenses:
                print("No expense found!")
                continue
            view_expense(filtered_expenses)
            break

        elif choice == 4:
            try:
                minimum_amount = int(input("Enter the amount : "))
                maximum_amount = int(input("Enter the amount : "))
            except ValueError:
                print("Invalid input . Please enter a valid number.")
                continue
            if minimum_amount > maximum_amount:
                print("Invalid input. Please try again.")
                continue
            filtered_expenses = filter_expenses_by_condition(
                expense_list,
                lambda expense: minimum_amount <= expense["amount"] <= maximum_amount
                )
            if not filtered_expenses:
                print("No expense found!")
                continue
            view_expense(filtered_expenses)
            break

        elif choice == 5:
            return

        else:
            print("Invalid choice. Please choose between 1 and 5.")
            
def filter_expenses_by_condition(expense_list, condition):
    filtered_expenses = []
    for expense in expense_list:
        if condition(expense):
            filtered_expenses.append(expense)
    return filtered_expenses