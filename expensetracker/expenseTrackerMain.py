
from llmconfig.LLMConfig import LLMModel
from datetime import datetime
with open("expensetracker/expenseTrackerPrompt.txt", "r") as file:
    EXPENSE_TRACKER_PROMPT = file.read()
TEXT_TO_BE_REPLACED_WITH_PROMPT = '[USER QUERY WILL BE APPENDED HERE]'
DELIMITER = "***"
class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def __str__(self):
        return f"{self.amount} | Category: {self.category} | Description: {self.description}, Date: {self.date}"
        return f"Expense(amount={self.amount}, category={self.category}, description={self.description}, date={self.date})"
def getExpenseDetailsFromLLM(prompt):
    llm = LLMModel()

    # Generate response using the LLM model
    response = llm.generate(prompt=EXPENSE_TRACKER_PROMPT.replace(TEXT_TO_BE_REPLACED_WITH_PROMPT,prompt))

    # Parse the response to extract expense details
    expense_details = response.split(DELIMITER)
    today = datetime.now().date()

    amount, category, description = expense_details
    return Expense(amount.strip(), category.strip(), description.strip(), today)

def writeExpenseToFile(expense):
    with open("expensetracker/expenses.txt", "a") as file:
        file.write(f"{expense.amount},{expense.category},{expense.description},{expense.date}\n")
def addExpenseFromPrompt(prompt):
    # Initialize the LLM model
   
    # Create an instance of the ExpenseTracker\
    # get todays date
    expense = getExpenseDetailsFromLLM(prompt)
    # Write the expense to the file
    writeExpenseToFile(expense)

    print(f"Expense added: {(expense)}")
    return f"Expense added: {expense.amount} | Category: {expense.category} | Description: {expense.description}, Date: {expense.date}"
def listExpenses():
    try:
        with open("expensetracker/expenses.txt", "r") as file:
            expenses = file.readlines()
            if not expenses:
                return "No expenses found."
            expensesList = [Expense(*line.strip().split(',')) for line in expenses]
            return "\n".join(str(expense) for expense in expensesList)
    except FileNotFoundError:
        return "No expenses found."