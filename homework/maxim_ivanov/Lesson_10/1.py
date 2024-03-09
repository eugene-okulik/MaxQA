# Задание №1
def finish_me(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("finished")

    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')


# Задание №2


def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs['count']
        for i in range(count):
            func(*args)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)

# Задание №3
num_1 = int(input('Enter a number: '))
num_2 = int(input('Enter another number: '))


def operation(func):
    def wrapper(*args):
        a, b = args[0], args[1]
        if a < 0 or b < 0:
            func(a, b, '*')
        elif a == b:
            func(a, b, '+')
        elif a > b:
            func(b, a, '-')
        elif a < b:
            func(a, b, '/')

    return wrapper


@operation
def calc(first, second, operation):
    if operation == '+':
        print(first + second)
    elif operation == '-':
        print(first - second)
    elif operation == '/':
        print(first / second)
    elif operation == '*':
        print(first * second)


calc(num_1, num_2)

# List comprehension
PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

list = list(PRICE_LIST.split())
list_key = [x for x in list[0::2]]
list_value = [int(x.replace('р', '')) for x in list[1::2]]
country_temps_dict = dict(zip(list_key, list_value))
