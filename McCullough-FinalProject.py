#Jeffrey McCullough
#May 2, 2022
#McCullough-FinalProject.py
#This is a program that creates a range based on input from a user and calculates if the numbers in the range are divisible by 3, 5, both, or neither.
#The program will return each number in the range and display the divisibility of the numbers.
def calc(minimum, maximum):
    for x in range(int(minimum), (int(maximum)+1)):
        if x%3 == 0 and x%5 == 0:
            print(x, 'is divisible by both 3 and 5')
        elif x%3 == 0:
            print(x,'is divisible by 3')
        elif x%5 == 0:
            print(x, 'is divisible by 5')
        else:
            print(x, 'is divisible by neither')
print('This app will take a range from numbers you enter and tell you whether they are divisible by 3, 5, both, or neither.\nPlease enter the following values.')
minimum = input('Enter a minimum value for your range of numbers: ')
while minimum.isnumeric() != True:
    minimum = input('Please enter a number. Only numbers can be divided: ')
maximum = input('Enter a maximum value for your range of numbers: ')
while maximum.isnumeric() != True:
    maximum = input('Please enter a number. Only numbers can be divided: ')
calc(minimum, maximum)

