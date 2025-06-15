num1=eval(input('Enter your first number:'))
num2=eval(input('Enter your second number:'))
print('choose your operation :+,-,x,/')
operation=str(input('Enter the operation:'))
if operation=='+':
    print(f'YOUR ANSWER IS:{num1+num2}')
elif operation=='-':
    print(f'YOUR ANSWER IS:{num1-num2}')
elif operation=='*' or operation=='x':
    print(f'YOUR ANSWER IS:{num1*num2}')
elif operation=='/':
    print(f'YOUR ANSWER IS:{num1/num2}')
else:
    print('Invalid Operation!')