limit = int(input("give the number: "))
tab = []
n = 2
while len(tab) < limit:
    for x in range(2, n):
        if (n % x) == 0:
            break
    else:
       tab.append(n)
    n += 1
print('prime number: ')
print(tab)