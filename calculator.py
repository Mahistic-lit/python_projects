num1=eval(input('Enter your first number:'))
num2=eval(input('Enter your second number:'))
operation=str(input('Enter the operation:'))
if operation=='+':
    print(num1+num2)
elif operation=='-':
    print(num1-num2)
elif operation=='*' or operation=='x':
    print(num1*num2)
elif operation=='%':
    print(num1%num2)
elif operation=='/':
    print(num1/num2)
else:
    print('Invalid Operation!')