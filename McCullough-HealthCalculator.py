#Jeffrey McCullough
#April 17, 2022
#LastName-HealthCalculator.py
#This is a program that calculates the body mass index and its classification based on the height and weight of the user.
#The program will also return 
intensity = [.5, .55, .6, .65, .7, .75, .8, .85, .9, .95]
length = len(intensity)
x = 0
def bmi(height, weight):
    bmi_calc = 703 * (int(weight) / (int(height)**2))
    bmi_calc = round(bmi_calc, 2)
    if int(bmi_calc) <= 18.5:
        index = ('Thin')
    elif int(bmi_calc) >= 18.6 and int(bmi_calc) <= 24.9:
        index = ('Healthy')
    elif int(bmi_calc) >= 25 and int(bmi_calc) <= 29.9:
        index = ('Overweight')
    else: index = ('Obese')
    print('\nYour results: \nYour BMI is:',round(bmi_calc,2), '--', index)
def rate_calc(age, rate):
    target_rate = ((((220 - int(age)) - int(rate)) * intensity[x]) + int(rate))
    target_rate = round(target_rate,0)
    print(str(int(float(intensity[x]) * 100)) + '%\t\t\t' + str(int(target_rate)), 'beats per minute')
print('Input the following values: ')
height = input('Height in inches: ')
while height.isnumeric() != True:
    height = input("Don't be silly, your height can't be measured like that. \nPlease use a positive number: ")
weight = input('Weight in pounds: ')
while weight.isnumeric() != True:
    weight = input("You weight that?! Not possible! \nPlease use a positive number: ")
age = input('Current age: ')
while age.isnumeric() != True:
    age = input("Age is typically measured using a positive number, since people can't age backwards. \nPlease use a positive number: ")
rate = input('Resting heart rate: ')
while rate.isnumeric() != True:
    rate = input("Heart rate is typically counted using a number. \nPlease use a positive number: ")
bmi(height, weight)
print('\nExercise Intensity \tMax Heart Rates:')
for x in range(length):
    rate_calc(age, rate)
print('\nGoodbye, and have a nice day!')
