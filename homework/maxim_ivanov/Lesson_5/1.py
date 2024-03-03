# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

# Задание 2
text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'

text1_pos = text1.index(':') + 1
text2_pos = text2.index(':') + 1
text3_pos = text3.index(':') + 1

text1_num = int(text1[text1_pos:].strip())
text2_num = int(text2[text2_pos:].strip())
text3_num = int(text3[text3_pos:].strip())

print(text1_num + 10)
print(text2_num + 10)
print(text3_num + 10)

# Задание 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students_list = ', '.join(students)
subjects_list = ', '.join(subjects)

print(f'Students {students_list} study these subjects: {subjects_list}')
