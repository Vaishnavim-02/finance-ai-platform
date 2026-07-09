def add_expense(expenses):
    print(" ADD EXPENSE ")
    continue_adding = True
    
    while continue_adding:
        expense_name=input("enter your shopping type: ")
        amount=int(input("enter the amount : "))
    
        expense = {
                        "expense":expense_name,
                        "amount":amount,
                        }
        expenses.append(expense)
        x = input("Do you want to add another expense ?")
        if( x == "no"):
                        continue_adding = False
    total = 0
    for expense in expenses:
                total = total + expense["amount"]
                print(expense["expense"])
                print(expense["amount"])
    print("Total : ", total)
expenses = []
def view_expense(expenses):

    if expenses != []:
        print("VIEW EXPENSE")

        total = 0

        for expense in expenses:
            total = total + expense["amount"]
            print(expense["expense"])
            print(expense["amount"])

        print("Total :", total)

    else:
        print("No expenses found.")

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
        add_expense(expenses)
    elif(choice=="2"):
        view_expense(expenses)
    elif(choice=="3"):
        print("Exit")
    else:
        print("Invalid Choice")

