from expenses import calculate_total

def spending_insights(expense_list):
    if not expense_list:
        print("No Expense Available.")
        return
    total = calculate_total(expense_list)
    print("=" * 35)
    print("      SPENDING INSIGHT")
    print("=" * 35)
    print(f"Total Spending : ₹{total}")
    print("=" * 35)
    highest_spending_category(expense_list)
    

def highest_spending_category(expense_list):
    category_total_spending = {}
    for expense in expense_list:
        category = expense["category"]
        amount = expense["amount"]
        if category in category_total_spending:
            category_total_spending[category] = category_total_spending[category] + amount
        else:
            category_total_spending[category] = amount
    highest_category = None
    highest_amount = 0
    for category, total in category_total_spending.items():
        if total > highest_amount:
            highest_amount = total
            highest_category = category
    print("=" * 35)
    print("   HIGHEST SPENDING CATEGORY")
    print("=" * 35)
    print(f"Category : {highest_category}")
    print(f"Amount   : ₹{highest_amount}")
    print("=" * 35)
            
def category_spending_percentage(expense_list):
    if not expense_list:
        print("No expense found.")
        return
    total = calculate_total(expense_list)
    category_total = {}
    for expense in expense_list:
        category = expense["category"]
        amount = expense["amount"]
        if category in category_total:
            category_total[category] = category_total[category]+ amount
        else:
            category_total[category] = amount
    print("=" * 35)
    print("   CATEGORY SPENDING %")
    print("=" * 35)
    for category,category_amount in category_total.items():
        percentage = (category_amount / total) * 100
        print(f"{category} : {percentage:.2f}%")
    print("=" * 35)
        