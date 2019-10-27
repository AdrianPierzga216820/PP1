n = int(input("give the number: "))
n2 = n
r = ''
while n >= 1:
    r = str(n % 2) + r
    print(f'{n:3}|{n % 2}')
    n = n // 2
print(f'{n2}(10)={r}(2)')