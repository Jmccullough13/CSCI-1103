import random
choices = ['rock', 'paper', 'scissors']
random_choice = random.choice(choices)
user_choice = ''
winner = ''
while (user_choice != 'rock' and
       user_choice != 'paper' and
       user_choice != 'scissors'):
    user_choice = input('Choose rock, paper, or scissors. ')
if user_choice == random_choice:
    winner = 'tie'
elif random_choice == 'paper' and user_choice == 'rock':
    winner = 'computer wins'
elif random_choice == 'rock' and user_choice == 'scissors':
    winner = 'computer wins'
elif random_choice == 'scissors' and user_choice == 'paper':
    winner = 'computer wins'
else:
    winner = 'you win'
print (f'You chose {user_choice} and the computer chose {random_choice}, {winner}')
