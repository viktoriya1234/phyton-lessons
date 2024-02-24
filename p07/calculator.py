print('Calculator')
is_run = True

while is_run:
    print("Actions:'+', '-', '*', '/', '^', Exit: 'x'")
    action = input('Action: ')
    result = 0
    number1 = float(input('Enter number1: '))
    number2 = float(input('Enter number2: '))
    action = input('Action: ')

    if action == 'x':
        is_run = False
    elif action == '+':
        result = number1 + number2
    elif action == '-':
        result = number1 - number2
    elif action == '*':
        result = number1 * number2
    elif action == '/':
        result = number1 / number2
    elif action == '^':
        result = number1 ** int(number2)
    else:
        print('Incorrect action: [', action, ']')

    print(f'{number1} {action} {number2}=', result)