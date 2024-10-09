def decorator_calc(func):
    def wrapper(*arg):
        first = arg[0]
        second = arg[1]
        if first == second:
            return func(first, second, "+")
        elif first > second:
            return func(first, second, "-")
        elif first < second:
            return func(first, second, "/")
        elif first < 0 or second < 0:
            return func(first, second, "*")
    return wrapper


@decorator_calc
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


res = calc(40, 5)
print(res)
res = calc(4, 5)
print(res)
res = calc(4, 4)
print(res)
res = calc(-4, 4)
print(res)
