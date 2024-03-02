# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

# Задание 2
text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'

text1_number = int(text1[text1.index('42'):])
text2_number = int(text2[text2.index('514'):])
text3_number = int(text3[text3.index('9'):])

print(text1_number + 10)
print(text2_number + 10)
print(text3_number + 10)

# Задание 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students_list = ', '.join(students)
subjects_list = ', '.join(subjects)

print(f'Students {students_list} study these subjects: {subjects_list}')
