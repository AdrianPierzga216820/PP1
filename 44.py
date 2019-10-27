l = int(input('speed limit: '))
p = int(input('give speed: '))
if (p - l) <= 10:
    print(f'fine: {(p - l) * 5} zł')
else:
    print(f'fine: {50 + ((p - l - 10) * 15)} zł')