#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv)
    if argc != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    if argv[2] not in ops:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    try:
        num1 = int(argv[1])
        num2 = int(argv[3])
    except ValueError:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)
    op = ops[argv[2]]
    result = op(num1, num2)
    print('{:d} {:s} {:d} = {:d}'.format(num1, argv[2], num2, result))
    exit(0)
