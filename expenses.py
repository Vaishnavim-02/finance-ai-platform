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