import random
import sys

sys.set_int_max_str_digits(0)


# Задание 1
def random_bonus():
    bonus = random.choice([True, False])
    salary = int(input("Enter your salary: "))
    if bonus:
        salary += bonus
        print(salary)


# Задание 2
def fibonacciGenerator(n):
    a = 0
    b = 1
    for i in range(n):
        yield b
        a, b = b, a + b


obj = fibonacciGenerator(100000)


def print_number():
    i = 1
    while 100000 >= i:
        num = next(obj)
        if i in [5, 200, 1000, 100000]:
            print(str(num))
        i += 1


print_number()
