# Задание №3

text1 = 'результат операции: 42'
text2 = 'результат операции: 54'
text3 = 'результат работы программы: 209'
text4 = 'результат: 2'


def numbers(*args):
    for arg in args:
        text_num = int(arg.split()[-1])
        print(text_num + 10)


numbers(text1, text2, text3, text4)
