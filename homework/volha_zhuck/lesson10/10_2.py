def repeat_me(func):
    def wrapper(*arg):
        text = arg[0]
        count = arg[1]
        for i in range(count):
            func(text)
        return
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', 6)
