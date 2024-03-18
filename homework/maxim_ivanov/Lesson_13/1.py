import os
import datetime
import locale

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', "hw_13", 'data.txt')


def read_file():
    with open(file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line


def func_date_something():
    for data_line in read_file():
        list_data = data_line.split(' ')
        date = list_data[1] + ' ' + list_data[2]
        current_date = datetime.datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S.%f')
        if list_data[0] == '1.':
            print(current_date + datetime.timedelta(days=7))
        elif list_data[0] == '2.':
            locale.setlocale(locale.LC_ALL, '')
            print(datetime.datetime.strftime(current_date, '%A').capitalize())
        elif list_data[0] == '3.':
            now = datetime.datetime.now()
            print((now - current_date).days)


func_date_something()
