def save_expense(amount, category, description):
    file = open("expenses.txt", "a")   # open the file in append mode
    file.write(str(amount) + "," + category + "," + description + "\n")
    file.close()                        # close the file manually

    print("Expense saved successfully!")
def show_expenses():
    total_expense = 0

    print("\n--- All Expenses ---")

    try:
        file = open("expenses.txt", "r")

        for line in file:
            data = line.strip().split(",")

            amount = int(data[0])
            category = data[1]
            description = data[2]

            total_expense = total_expense + amount

            print("₹", amount, "|", category, "|", description)

        file.close()
        print("\nTotal Expense: ₹", total_expense)

    except:
        print("No expense data found!")
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        amount = int(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

        save_expense(amount, category, description)

    elif user_choice == "2":
        show_expenses()

    elif user_choice == "3":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Please enter a valid option!")