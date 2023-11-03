#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div


if len(sys.argv) != 4:
    print("usage: {} <a> <operator> <b>".format(sys.argv[0]))
    sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])


operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div,
    }
if operator in operators:
    result = operators[operator](a, b)
    print('{} {} {} = {}'.format(a, operator, b, result))
else:
    print('Unknown operator. Available operators: +, -, *, and /')
    sys.exit(1)
