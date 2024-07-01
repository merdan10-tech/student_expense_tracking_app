from expense import Expense

#used to indentify today's date
import calendar
import datetime

def main():
    print("Welcome to the Student Expense Tracker 🎬")
    path_to_file = "expenses.csv"
    budget = 2000

    #Get user input of expense
    expense = get_user_input()

    #Store expenses into a file
    save_expense_to_file(expense, path_to_file)

    #Read file and summarize expenses
    summarize_expense_to_file(path_to_file, budget)

def get_user_input():
    #to get inputs from user on name and amount of item
    print("Getting User Expense! 💰")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount ($): "))

    expense_category = [
        "📖 Education",
        "🍔 Dining",
        "😜 Entertainment",
        "🚗 Transportation",
        "✨ Miscellaneous"
    ]
    #to loop infinitely
    while True:
        print("Select a category: ")
        #to enumarate items in the list
        for index, expense in enumerate(expense_category, start=1):
            print(f"   {index}. {expense}")

        value_range = f"[1 - {len(expense_category)}]"
        # we subtracted 1 bc we added 1 to enumeration earlier. we need it to balance out the count
        selected_index = int(input(f"Enter a category number {value_range}: ")) -1

        #to verify if the input in the range
        if selected_index in range(len(expense_category)):
            selected_category = expense_category[selected_index]

            #create an object for our attributes
            new_expense = Expense(
                name=expense_name, amount=expense_amount, category=selected_category
            )
            return new_expense
        else:
            print("Invalid Category. Please try again")

#creating a file and passing expenses
def save_expense_to_file(expense, path_to_file):
    with open(path_to_file, "a", encoding="utf-8") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")

#getting back the expenses and summarizing by doing calculations
def summarize_expense_to_file(path_to_file, budget):
    print("Summarize User Expense! 🎯")

    #list to store extracted expenses
    expenses = []
    with open(path_to_file, "r", encoding="utf-8") as f:
        #to read each line of the file
        lines = f.readlines()

        #striped and splitted to pass it to the list
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense (
                name=expense_name, amount=float(expense_amount), category=expense_category
            )
            expenses.append(line_expense)

    #dict to put category as a key , and amount as a value
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Category 📈: ")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    #calc total spent
    total_spent = sum([ex.amount for ex in expenses])
    print(f"💵 Total spent ${total_spent:.2f} this month!")

    #remaining budget calc
    remaining_budget = budget - total_spent
    print(f"️☑️ Budget remaining ${remaining_budget:.2f} this month!")

    # Get the current date
    now = datetime.datetime.now()
    # Get the number of days in the current month
    days_in_the_month = calendar.monthrange(now.year, now.month)[1]
    # Calculate the remaining number of days in the current month
    remaining_days = days_in_the_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(f"Budget per day: ${daily_budget}")


if __name__ == "__main__":
    main()