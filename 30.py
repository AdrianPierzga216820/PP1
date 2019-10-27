for x in range(3):
    if input("enter your PIN number: ") == '0805':
        print('it works')
        break
    else:
        print('incorect PIN.')
    if x == 2:
        print('the card has been declined.')