import random
comp_choice=random.randint(1,99)
print("🎲 I'M THINKING OF A NUMBER BETWEEN 1 TO 99. TRY TO GUESS IT! ")
attempts=1
try:  
    user_choice=int(input("GUESS THE NUMBER: "))
    while user_choice!=comp_choice:
        if user_choice<comp_choice:
            print('OOPS!,THE NUMBER YOU HAVE GUESSED IS A LITTLE LOW.TRY AGAIN!')
        elif user_choice>comp_choice:
            print('OOPS!,THE NUMBER YOU HAVE GUESSED IS A LITTLE HIGH.TRY AGAIN!')
        attempts+=1
        user_choice=int(input('Guess the number: '))
    if user_choice==comp_choice:
        print('🎉CONGRATULATIONS!!!,YOU HAVE GUESSED THE NUMBER!')
        print(f'YOU HAVE GUESSED THE NUMBER IN {attempts} ATTEMPTS')
except ValueError:
            print('⚠️PLEASE ENTER THE VALID WHOLE INPUT!')