a = int(input('set a: '))
b = int(input('set b: '))
for x in range(1, a + 1):
    if x == 1 or x == a:
        print("*" * b)
    else:
        print("*" + " " * (b - 2) + "*")