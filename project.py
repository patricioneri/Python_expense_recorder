import pandas as pd
import re

"""Define recorder class"""
class Recorder():
    """initial data of the recorder"""
    def __init__(self, amount = 0):
        self._balance = amount #Balance of money
        self._expenses = [] #List of expenses

    """Add a new expense"""
    def new_expense(self, expense, date, description):
        self._balance -= expense #substract the expense to the balance
        self._expenses.append([date, expense, description]) #Add the expense

    """Add new income"""
    def new_income(self, income):
        self._balance += income #Add income to the balance

    """Show the expenses"""
    def view_expenses(self):
        print('Expense summary')
        print(f'Account balance: {self._balance}') #Print account balance
        for expense in self._expenses: #Iterate the expenses and print it
            print(expense)

    """Erase a expense"""
    def erase_expense(self):
        id = 0 #Add id to the expenses
        for expense in self._expenses: #Iterate the expenses
            print(id, end=" ") #Print id for each expense
            print(expense)
            id += 1
        id_delete = int(input('Enter id of the expense you want to erase: ')) #Ask for the id of the desire expense
        self._balance = self._balance + self._expenses[id_delete][1] #Add amount of expense to balance
        del self._expenses[id_delete] #Delete the expense

    """Donwnload csv"""
    def download_csv(self):
        df = pd.DataFrame(self._expenses, columns = ['Date', 'Expense', 'Description']) #Create pandas DataFrame
        df.to_csv('Expenses', index = False) #Transform df to csv
        print('Data has been saved to Expenses.csv')

def menu():
    return '''Press: \n 1: Enter a new expense. \n 2: Enter a new income. \n 3: View the expenses. \n 4: Erase a expense. \n 5: Download a csv file with the expenses. \n 6: Exit. \n ================================= '''


def initialization():
    return 'Welcome to expense recorder \n ================================= \n Initializing...'


"""Select the desire option and call the method"""
def selection(number,recorder):
        while True:
            if number == 1:
                """Add new expense - Method call and error checking"""
                try:
                    expense = int(input('Expense amount: '))
                except ValueError:
                    print('Invalid expense. Enter expense again.')
                    selection(number,recorder)
                try:
                    date = input('Date (yyyy-mm-dd ): ')
                    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
                        raise ValueError
                except ValueError:
                    print('Invalid date format.Enter expense again.')
                    selection(number,recorder)
                description = input('Description: ')
                recorder.new_expense(expense, date, description)
                print('Expense entered succesfully')

            elif number == 2:
                """""Add new income - Method call and error checking"""""
                try:
                    income = int(input('Income amount: '))
                    recorder.new_income(income)
                except ValueError:
                    selection(number,recorder)

            elif number == 3:
                """View expenses - Method call"""
                recorder.view_expenses()

            elif number == 4:
                """Erase expense - Method call"""
                recorder.erase_expense()

            elif number == 5:
                """Download csv - Method call"""
                recorder.download_csv()

            elif number == 6:
                return 'Program finished'
            print(menu())
            number = int(input())


def main():
    print(initialization()) #Initialize program
    amount = int(input('Enter the money in your account: ')) #Ask for initial user's money
    recorder = Recorder(amount) #Instantiate recorder
    print(menu()) #show menu
    number = int(input())
    selection(number, recorder) #Invoke selector with the respective method call


if __name__ == "__main__":
    main()