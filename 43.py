tab = []
for x in range(1, 4):
    tab.append(int(input(f"give {x} the: ")))
print(f'sorted: {", ".join([str(x) for x in sorted(tab)])}')