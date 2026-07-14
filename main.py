import expenses
from expenses import load_expenses

expense_list = load_expenses()

while True:

    print("=" * 35)
    print(" AI PERSONAL FINANCE PLATFORM ")
    print("=" * 35)
    print("=" * 35)
    print(" 1. ADD EXPENSE ")
    print("=" * 35)
    print("=" * 35)
    print(" 2. VIEW EXPENSE ")
    print("=" * 35)
    print("=" * 35)
    print(" 3. EXIT ")
    print("=" * 35)
    
    choice=input("Enter your choice :")
    print(choice)
    if(choice=="1"):
        expenses.add_expense(expense_list)
    elif(choice=="2"):
        expenses.view_expense(expense_list)
    elif(choice=="3"):
        print(" Exiting AI PERSONAL FINANCE PLATFORM ")
        break
    else:
        print("Invalid Choice")
