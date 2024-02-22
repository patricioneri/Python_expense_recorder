# Expense recorder
#### Video Demo:  https://youtu.be/fH-6J2DZXD4
#### Description:
##### Intro
My apologies for that oversight. Let me enhance the text by incorporating additional words:

This code was created by me, Patricio Garcia, as my final project for the CS50 Python course. I developed an expense recorder using Python and the Pandas library. I decided to utilize Object-Oriented Programming for developing the recorder. The `Recorder` class instantiates recorder objects that emulate a real-life recorder, allowing users to register their expenses and available funds.

The program consists of three functions: one for printing the initial message, a second one for displaying the option menu, and a third one containing conditionals for each action. Initially, the program prompts the user for the initial amount of money in the account (function 1). Subsequently, the program instantiates the recorder with this information and an empty list for the user to fill with expenses. Then, the program displays six options on the screen (function 3). Upon the user selecting a number, the program enters the third function, which contains a while loop with several conditionals inside, invoking the selected method:

1. **Enter a new expense:** If the entered number equals one, the program enters a conditional that calls a method to record a new expense in the expense list of the recorder object. Additionally, error checking is implemented using try/except to prompt the user to enter data in the correct form. For ensuring the correct date format, the program uses regex to compare the entered date against the correct date format.

2. **Enter a new income:** If the entered number equals two, the program enters a conditional that calls a method to add a new income to the account balance. There is also a try/except block to handle ValueError and prompt the user again if the entered income value is incorrect.

3. **View the expenses:** If the entered number equals three, the program enters a conditional that calls a method to print a summary with the date and description of each expense. To achieve this, the method contains a for loop iterating through the list of expenses in the recorder object.

4. **Erase an expense:** If the entered number equals four, the program enters a conditional that calls a method to iterate through the list of expenses, assigning an ID number to each, and prints the expenses. Then, the method prompts the user for the ID of the expense to erase.

5. **Download a CSV file with the expenses:** If the entered number equals five, the program enters a conditional that calls a method for downloading the expenses in CSV format. For this purpose, the program utilizes the Pandas library. Initially, a DataFrame is created with the data, which is then converted and downloaded as a CSV file.

6. **Exit:** If the entered number equals six, the program enters a conditional that terminates the function selection, which includes the while cycle, returning a 'Program finished' message.

This code applies several concepts learned during CS50 such as loops, condicional, Object Oriented Programming, error capture, regex and functions. Futhermore, the code use some extra features as Pandas library for downloading the data. As conclusion, the concepts of the course was implemented in a functional Python application.