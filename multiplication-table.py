#printing a multiplication table
try: 
    num=int(input('Enter the number: '))
    for i in range(1,11,1):
        print(f'{num} x {i} = {num*i}')
except ValueError :
    print('Invalid input!')