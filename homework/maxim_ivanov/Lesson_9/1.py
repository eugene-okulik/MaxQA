# Обработка даты
import datetime

from statistics import fmean

my_date = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')
print(python_date.strftime('%B'))
print(python_date.strftime('%d.%m.%Y, %H:%M'))

# Map, filter
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]


def hot_temperatures(temperatures):
    return temperatures > 28


list_of_temperatures = list(filter(hot_temperatures, temperatures))

print(f'Max temperature: {max(list_of_temperatures)}')
print(f'Min temperature: {min(list_of_temperatures)}')
print(f'Avg temperature: {round(fmean(list_of_temperatures))}')
