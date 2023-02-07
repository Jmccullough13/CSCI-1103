#Jeffrey McCullough
#April 4, 2022
#LastName-HiLoGame.py
#This is a number gussing game.
#The game asks the user to set a maximum limit for the computer to guess from.
#The game picks a random number in the range of 1 and the maximum number, then asks the user to guess the number the game picked.
import random
n = int(input('What should the maximum number for this game be? '))
random = int(random.randint(1,n))
x = ''
winner = ''
again =  'y'
while again.lower() == 'y':
    x = int(input('\nGuess my number: '))
    while x > n or x < 1  or x == 0:
        x = int(input('\nGuess my number: '))
    while (x != random
           and x >= 1
           and x <= n):
        if x > random:
            print('Your guess is too high.\n')
            x = int(input('Guess my number: '))
        if x < random:
            print('Your guess is too low.\n')
            x = int(input('Guess my number: '))
        if x == random:
            break
    if x == random:
        print('You guessed my number!\n')
        again = input('Do you wish to play again? (Y/N): ')
    if again == 'y':
        n = int(input('\nWhat should the maximum number for this game be? '))
        print()
    if again == 'n':
        print('\nThank you for playing!')
    while again != 'n' and again != 'y':
        again = input('\nDo you wish to play again? (Y/N): ')






