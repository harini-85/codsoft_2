def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

op_sym = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

def calculator():
    n1 = int(input('Enter first number: '))
    for i in op_sym:
        print(i)
    flag = True
    while flag:
        op = input('Pick an operation: ')
        n2 = int(input('Enter next number: '))
        calcfnctn = op_sym[op]
        output = calcfnctn(n1, n2)
        print(f'{n1} {op} {n2} = {output}')

        ask = input(f'Enter y to continue calculation with {output} \nEnter n to start new calculation \nEnter x to exit: ')

        if ask == 'y':
            n1 = output
        elif ask == 'n':
            flag = False
            calculator()
        else:
            flag = False
            print('Thank You!')

calculator()