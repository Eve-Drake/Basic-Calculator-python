

def calculate():
    value1 = int(input(''))
    operation = input('')
    value2 = int(input(''))
    total = 0
    if operation == '*':
        total = value1 * value2
    elif operation == '/':
        total = value1 / value2
    elif operation == '-':
        total = value1 - value2
    elif operation == '+':
        total = value1 + value2
    else:
        print('Please enter a valid operation :  +-*/')
    print(total)

calculate()