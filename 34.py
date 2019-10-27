p = input('personal number: ')
print(f"sex: {'male' if int(p[-2]) % 2 else 'female'}")
print(f'age: {118 - int(p[:2])}')