import random
comp_choice=random.randint(1,99)
print("🎲 I'M THINKING OF A NUMBER BETWEEN 1 TO 99. TRY TO GUESS IT! ")
#to calculate the number of attempts.
attempts=1
try:  
#asking for user input
    user_choice=int(input("GUESS THE NUMBER: "))
#using while loop, if the user guessed the wrong number
    while user_choice!=comp_choice:
        if user_choice<comp_choice:
            print('OOPS!,THE NUMBER YOU HAVE GUESSED IS A LITTLE LOW.TRY AGAIN!')
        elif user_choice>comp_choice:
            print('OOPS!,THE NUMBER YOU HAVE GUESSED IS A LITTLE HIGH.TRY AGAIN!')
#increasing th number of attempts
        attempts+=1
        user_choice=int(input('Guess the number: '))
#if the user correctly guessed the number
    if user_choice==comp_choice:
        print('🎉CONGRATULATIONS!!!,YOU HAVE GUESSED THE NUMBER!')
        print(f'YOU HAVE GUESSED THE NUMBER IN {attempts} ATTEMPTS')
#incase user inputs invalid input
except ValueError:
            print('⚠️PLEASE ENTER THE VALID WHOLE INPUT!')
#The program asks the user to guess the number between 1 to 99.
#It will run until,the user guesses the correct number.
#It will show the number of attempts user took to guess the number correctly.
