import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
add_group = ("insert into `groups` (title, start_date, end_date) values (%s,%s, %s)")
data_group = ('MFT-2', '15.03.2024', '15.03.2026')
cursor.execute(add_group, data_group)
group_id = cursor.lastrowid

add_student = ("insert into `students` (name, second_name, group_id) values (%(name)s,%(second_name)s, %(group_id)s)")
data_student = {
    'name': 'Mark',
    'second_name': 'Ivanov',
    'group_id': group_id
}
cursor.execute(add_student, data_student)
student_id = cursor.lastrowid

add_book = ("insert into `books` (title, taken_by_student_id) values (%(title)s, %(student_id)s)")
data_book = {
    'title': 'Новая жизнь',
    'student_id': student_id,
}
data_book_2 = {
    'title': 'Старая жизнь',
    'student_id': student_id,
}
cursor.execute(add_book, data_book)
cursor.execute(add_book, data_book_2)

add_subjets = ("insert into subjets  (title) values (%(title)s)")
data_subjets = {
    'title': 'Наследие людей',
}
data_subjets_2 = {
    'title': 'Наследие зверей',
}
cursor.execute(add_subjets, data_subjets)
subjects_1_id = cursor.lastrowid

cursor.execute(add_subjets, data_subjets_2)
subjects_2_id = cursor.lastrowid

add_lessons = ("insert into lessons  (title, subject_id) values (%(title)s, %(subject_id)s)")
data_lessons = {
    'title': 'Наследие людей начало',
    'subject_id': subjects_1_id
}
data_lessons_2 = {
    'title': 'Наследие зверей начало',
    'subject_id': subjects_2_id
}
data_lessons_3 = {
    'title': 'Наследие зверей продолжение',
    'subject_id': subjects_2_id
}
data_lessons_4 = {
    'title': 'Наследие людей продолжение',
    'subject_id': subjects_1_id
}
cursor.execute(add_lessons, data_lessons)
data_lessons_id = cursor.lastrowid

cursor.execute(add_lessons, data_lessons_2)
data_lessons_2_id = cursor.lastrowid

cursor.execute(add_lessons, data_lessons_3)
data_lessons_3_id = cursor.lastrowid

cursor.execute(add_lessons, data_lessons_4)
data_lessons_4_id = cursor.lastrowid

add_marks = ("insert into marks (value , lesson_id, student_id) values (%(value)s, %(lesson_id)s, %(student_id)s)")
data_marks = {
    'value': '9',
    'lesson_id': data_lessons_id,
    'student_id': student_id
}
data_marks_2 = {
    'value': '7',
    'lesson_id': data_lessons_2_id,
    'student_id': student_id
}
data_marks_3 = {
    'value': '5',
    'lesson_id': data_lessons_3_id,
    'student_id': student_id
}
data_marks_4 = {
    'value': '5',
    'lesson_id': data_lessons_4_id,
    'student_id': student_id
}
cursor.execute(add_marks, data_marks)
cursor.execute(add_marks, data_marks_2)
cursor.execute(add_marks, data_marks_3)
cursor.execute(add_marks, data_marks_4)

query = ("SELECT m.value from marks m join students s on m.student_id = s.id WHERE s.id = %(student_id)s")

data_query = {"student_id": student_id}
cursor.execute(query, data_query)
print(cursor.fetchall())

query_2 = ("SELECT * from books b join students s on b.taken_by_student_id = s.id WHERE s.id = %(student_id)s")

cursor.execute(query_2, data_query)
print(cursor.fetchall())

query_3 = ("SELECT * from students s join marks m on s.id = m.student_id join books b on s.id = b.taken_by_student_id "
           "WHERE  s.id = %(student_id)s")
cursor.execute(query_3, data_query)
print(cursor.fetchall())

db.commit()
db.close()
