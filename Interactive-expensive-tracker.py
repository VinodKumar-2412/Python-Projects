def display_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Monthly Total")
    print("4. View Category Summary")
    print("5. Exit")

def add_expense(expenses):
    try:
        amount = float(input("Enter amount spent: $"))
        if amount <= 0:
            print("Amount must be greater than 0!")
            return
        
        category = input("Enter category (food/transport/utilities/other): ").lower()
        date = input("Enter date (DD/MM/YYYY): ")
        
        # Basic date validation
        try:
            day, month, year = date.split('/')
            if not (1 <= int(day) <= 31 and 1 <= int(month) <= 12):
                print("Invalid date format!")
                return
        except:
            print("Invalid date format! Please use DD/MM/YYYY")
            return
            
        description = input("Enter description: ")
        
        expense = {
            'amount': amount,
            'category': category,
            'date': date,
            'description': description
        }
        
        expenses.append(expense)
        print("\nExpense added successfully!")
        
    except ValueError:
        print("Please enter a valid amount!")

def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded yet!")
        return
        
    print("\n=== All Expenses ===")
    for i, expense in enumerate(expenses, 1):
        print(f"\nExpense #{i}:")
        print(f"Amount: ${expense['amount']:.2f}")
        print(f"Category: {expense['category']}")
        print(f"Date: {expense['date']}")
        print(f"Description: {expense['description']}")

def monthly_total(expenses):
    if not expenses:
        print("\nNo expenses recorded yet!")
        return
        
    month = input("Enter month (MM/YYYY): ")
    try:
        month_num, year = month.split('/')
    except:
        print("Invalid format! Please use MM/YYYY")
        return
        
    total = 0
    for expense in expenses:
        if expense['date'].split('/')[1:] == [month_num, year]:
            total += expense['amount']
    
    print(f"\nTotal expenses for {month}: ${total:.2f}")

def category_summary(expenses):
    if not expenses:
        print("\nNo expenses recorded yet!")
        return
        
    categories = {}
    for expense in expenses:
        cat = expense['category']
        categories[cat] = categories.get(cat, 0) + expense['amount']
    
    print("\n=== Category Summary ===")
    for category, amount in categories.items():
        print(f"{category.capitalize()}: ${amount:.2f}")

def main():
    expenses = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            monthly_total(expenses)
        elif choice == '4':
            category_summary(expenses)
        elif choice == '5':
            print("\nThank you for using Expense Tracker!")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()