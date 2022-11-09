while(True):
    print('''What do you want to do?\n
    Press (+) for SUM\n
    Press (-) for SUBSTRACTION\n
    Press (/) for DIVISION\n 
    Press (*) for MULTIPLICATION\n   
    Press (e) for EXIT:\n ''')
    a = input()
    if a == 'e':
        quit()
    else:
        b = int(input("Enter the first number: \n"))
        c = int(input("Enter the second number: \n"))
        if a == '+':
            d = b + c
            print(f"{b} {a} {c} = {d}")
        elif a == '-':
            d = b - c
            print(f"{b} {a} {c} = {d}")
        elif a == '/':
            d = b / c
            print(f"{b} {a} {c} = {d}")
        elif a == '*':
            d = b * c
            print(f"{b} {a} {c} = {d}")
