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
    print(" 3. DELETE EXPENSE ")
    print("=" * 35)
    print("=" * 35)
    print(" 4. EDIT EXPENSE ")
    print("=" * 35)
    print("=" * 35)
    print(" 5. SEARCH EXPENSE ")
    print("=" * 35)
    print("=" * 35)
    print(" 6. CATEGORY SUMMARY ")
    print("=" * 35)
    print("=" * 35)
    print(" 7. HIGHEST EXPENSE")
    print("=" * 35)
    print("=" * 35)
    print(" 8. LOWEST EXPENSE")
    print("=" * 35)
    print("=" * 35)
    print(" 9. AVERAGE EXPENSE")
    print("=" * 35)
    print("=" * 35)
    print("10. TOTAL EXPENSES")
    print("=" * 35)
    print("=" * 35)
    print("11. EXPENSE PERCENTAGE")
    print("=" * 35)
    print("=" * 35)
    print("12. SORT EXPENSES")
    print("=" * 35)
    print("=" * 35)
    print("13. EXIT")
    print("=" * 35)
        
    choice=input("Enter your choice :")
    print(choice)
    if(choice=="1"):
        expenses.add_expense(expense_list)
    elif(choice=="2"):
        expenses.view_expense(expense_list)
    elif(choice=="3"):
        expenses.delete_expense(expense_list)
    elif(choice=="4"):
        expenses.edit_expense(expense_list)
    elif(choice=="5"):
        expenses.search_expense(expense_list)
    elif(choice=="6"):
        expenses.category_summary(expense_list)
    elif(choice=="7"):
        expenses.highest_expense(expense_list)
    elif(choice=="8"):
        expenses.lowest_expense(expense_list)
    elif(choice=="9"):
        expenses.average_expense(expense_list)
    elif(choice=="10"):
        expenses.total_number_of_expenses(expense_list)
    elif(choice=="11"):
        expenses.expense_percentage(expense_list)
    elif(choice=="12"):
            expenses.sort_expenses(expense_list)
    elif(choice=="13"):
            print(" Exiting AI PERSONAL FINANCE PLATFORM ")
            break
    else:
        print("Invalid Choice")
