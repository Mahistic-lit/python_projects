import random
print('''
Lets play the 'Rock','Paper','Scissors' game with computer!
The computer has already decided its move!
NOW ITS YOUR TURN!!!
''')
choices=['rock','paper','scissors']
comp_choice=random.choice(choices)
for index,words in enumerate(choices,start=1):
    print(index,words)
player_choice=str(input('choose between given list:'))
player_choices=player_choice.lower()
if player_choices!='rock' and player_choices!='paper' and player_choices!='scissors':
    print("INVALID CHOICE,PLEASE SELECT BETWEEN 'ROCK','PAPER','SCISSORS'")
    exit()
if player_choices=='rock' and comp_choice=='scissors':
    print(f'CONGRATULATIONS!,YOU WIN!!,computer choose {comp_choice}')
elif player_choices=='rock' and comp_choice=='paper':
    print(f'OPPS!,COMPUTER WINS!!,computer choose {comp_choice}')
elif player_choices=='paper' and comp_choice=='rock':
    print(f'CONGRATULATIONS!,YOU WIN!!,computer choose {comp_choice}')
elif player_choices=='paper' and comp_choice=='scissors':
    print(f'OPPS!,COMPUTER WINS!!,computer choose {comp_choice}')
elif player_choices=='scissors' and comp_choice=='rock':
    print(f'OPPS!,COMPUTER WINS!!,computer choose {comp_choice}')
elif player_choices=='scissors' and comp_choice=='paper':
    print(f'CONGRATULATIONS!,YOU WIN!!,computer choose {comp_choice}')
else:
    print(f'ITS A TIE,')
    
