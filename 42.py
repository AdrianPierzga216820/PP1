x = int(input('give the number: '))
y = int(input('give the number: '))
try:
    print(f'result: {x/y}')
except ZeroDivisionError:
    print('dividing by 0!')