#Jeffrey McCullough
#3/27/2022
#McCullough-Calculator
#This program asks a user to choose a mathematical operation and numbers and returns the calculation of the numbers using the operation.
operation = input('Please select one option: add/subtract/multiply/divide.')
print ('You chose', operation)
number1 = input('What is your first number?')
number2 = input('What is your second number?')
if operation == 'add':
    print(number1,'+',number2,'=',float(number1) + float(number2))
elif operation == 'subtract':
    print(number1,'-',number2,'=',float(number1) - float(number2))
elif operation == 'multiply':
    print(number1,'*',number2,'=',float(number1) * float(number2))
elif operation == 'divide':
    print(number1,'/',number2,'=',float(number1) / float(number2))
else:
    print ('The option you chose (' + operation + ') is not valid. \nPlease try this program again.')
