  
tab = []
while True:
    x = int(input("give the number: "))
    if x == 0:
        print(f'result: number={len(tab)}, Sum={sum(tab)}, average={sum(tab) / len(tab)}')
        break
    tab.append(x)