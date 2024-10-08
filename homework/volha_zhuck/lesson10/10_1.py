def finish_me(func):


    def wrapper(*arg):
        result = func(*arg)
        print('finished')
        return result
    

    return wrapper
    

@finish_me
def print1():
    print('print anything')


@finish_me
def example(text):
    print(text)


example('print me')
print1()
