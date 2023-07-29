def sum_(n1, n2):
    return n1+n2    


def minus(n1, n2):
    return n1-n2


def times(n1, n2):
    return n1*n2


def division(n1, n2):
    return n1/n2


def operation(signal):
    if signal == '+':
        result = sum_(number_1, number_2)
        return f'{result:.2f}'
    if signal == '-':
        result = minus(number_1, number_2)
        return f'{result:.2f}'
    if signal == '*':
        result = times(number_1, number_2)
        return f'{result:.2f}'
    if signal == '/':
        result = division(number_1, number_2)
        return f'{result:.2f}'

import art
print(art.logo)
number_1 = float(input("What's the first number?: "))
number_2 = float(input("What's the next number?: "))
signal = input('+\n-\n*\n/\nPick an operation: ')

print(f'{number_1}{signal}{number_2} = {operation(signal)}')