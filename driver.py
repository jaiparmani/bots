from expensetracker.expenseTrackerMain import addExpenseFromPrompt


def main():
    addExpenseFromPrompt(input("Enter expense -"))
if __name__ == '__main__':
    while(True):
        main()