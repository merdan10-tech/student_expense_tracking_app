<h1>Student Expense Tracker</h1>

<h2>Description</h2>
This project is a Student Expense Tracking App designed to help students manage their expenses effectively. The application allows users to input their expenses, categorize them, and get a summary of their spending, helping them stay within their budget.

<h2>Features:</h2>
User-Friendly Interface:

Welcome Message: Greets the user with a welcoming message.
User Input: Prompts the user to input the name, amount, and category of the expense.


<h2>Expense Categories:</h2>

Provides predefined categories for expenses, such as Education, Dining, Entertainment, Transportation, and Miscellaneous.

<h2>Expense Storage:</h2>

Stores expenses in a CSV file (expenses.csv) for easy access and persistence.

<h2>Expense Summary:</h2>

- <b>Reads the stored expenses from the CSV file.</b>
- <b>Summarizes expenses by category, displaying the total amount spent in each category.</b>
- <b>Calculates and displays the total amount spent for the current month.</b>
- <b>Calculates the remaining budget and the daily budget for the rest of the month.</b>

<h2>Code Overview:</h2>

- <b>Main Function:</b>

Welcomes the user and initiates the process by getting user input, storing the expense, and summarizing the expenses.

- <b>User Input Function:</b>

Prompts the user for the expense name, amount, and category.
Validates the category input and creates an Expense object.

- <b>Save Expense Function:</b>

Appends the user input to a CSV file for persistence.

- <b>Summarize Expense Function:</b>

Reads and parses the CSV file to retrieve stored expenses.
Aggregates expenses by category and calculates total spending.
Computes the remaining budget and the daily budget based on the current date and remaining days in the month.
