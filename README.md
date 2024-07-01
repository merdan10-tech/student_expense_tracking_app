Student Expense Tracker
This project is a Student Expense Tracking App designed to help students manage their expenses effectively. The application allows users to input their expenses, categorize them, and get a summary of their spending, helping them stay within their budget.

Features:
User-Friendly Interface:

Welcome Message: Greets the user with a welcoming message.
User Input: Prompts the user to input the name, amount, and category of the expense.
Expense Categories:

Provides predefined categories for expenses, such as Education, Dining, Entertainment, Transportation, and Miscellaneous.
Expense Storage:

Stores expenses in a CSV file (expenses.csv) for easy access and persistence.
Expense Summary:

Reads the stored expenses from the CSV file.
Summarizes expenses by category, displaying the total amount spent in each category.
Calculates and displays the total amount spent for the current month.
Calculates the remaining budget and the daily budget for the rest of the month.
Code Overview:
Main Function:

Welcomes the user and initiates the process by getting user input, storing the expense, and summarizing the expenses.
User Input Function:

Prompts the user for the expense name, amount, and category.
Validates the category input and creates an Expense object.
Save Expense Function:

Appends the user input to a CSV file for persistence.
Summarize Expense Function:

Reads and parses the CSV file to retrieve stored expenses.
Aggregates expenses by category and calculates total spending.
Computes the remaining budget and the daily budget based on the current date and remaining days in the month.
