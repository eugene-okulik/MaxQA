import os
from dotenv import load_dotenv
import mysql.connector as mysql
import csv

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', "hw_data", 'data.csv')

load_dotenv()

db = mysql.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

new_data = []

with open(file_path, encoding='UTF-8', newline='') as csvfile:
    data = csv.DictReader(csvfile, delimiter=',')
    for row in data:
        new_data.append(row)


def search_students(list_students):
    cursor = db.cursor(dictionary=True)
    for student in list_students:
        query = ("SELECT * from students s "
                 "join `groups` g on s.group_id = g.id "
                 "join books b on b.taken_by_student_id = s.id "
                 "join marks m on m.student_id = s.id "
                 "join lessons l on m.lesson_id = l.id "
                 "join subjets s2 on l.subject_id = s2.id "
                 "WHERE s.name = %(name)s and s.second_name = %(second_name)s "
                 "and g.title = %(group_title)s "
                 "and b.title  = %(book_title)s "
                 "and m.value = %(mark_value)s "
                 "and l.title = %(lesson_title)s "
                 "and s2.title = %(subject_title)s")

        data_student = {
            'name': student['name'],
            'second_name': student['second_name'],
            'group_title': student['group_title'],
            'book_title': student['book_title'],
            'mark_value': student['mark_value'],
            'lesson_title': student['lesson_title'],
            'subject_title': student['subject_title']
        }
        cursor.execute(query, data_student)

        output = cursor.fetchone()
        if output is None:
            print(student)


search_students(new_data)
db.close()
