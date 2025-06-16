#defining a function
def maximum(a,b):
    if a>b:
        print(f'The maximum number is:{a}')
    elif a<b:
        print(f'The maximum number is :{b}')
#if both numbers are same
    else:
        print('Both numbers are same')
#using while loop to input the corrct value from the user
while True:
    try:
        num1=float(input('Enter the first number: '))
        num2=float(input('Enter the second number: '))
        maximum(num1,num2)
        break
#if user put an invalid input5
    except ValueError:
        print('Invalid input')
