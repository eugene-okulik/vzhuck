import csv
import mysql.connector as mysql
import os
import dotenv

dotenv.load_dotenv()

with open(
    './homework/eugene_okulik/Lesson_16/hw_data/data.csv',
    newline=''
) as csv_file:
    file_data = csv.reader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

for row in data:
    name, second_name, group_title, book_title, \
        subject_title, lesson_title, mark_value = row
    cursor = db.cursor(dictionary=True)
    select_query = f'''
            SELECT *
            FROM students s
            left JOIN books b ON b.taken_by_student_id = s.id
            left JOIN marks m ON m.student_id = s.id
            left join lessons l ON l.id = m.lesson_id
            left join subjets sub ON sub.id = l.subject_id
            left JOIN `st-onl`.groups on `st-onl`.groups.id = s.group_id
            WHERE s.name = '{name}' and s.second_name = '{second_name}'
            and b.title = '{book_title}' and sub.title = '{subject_title}'
            and l.title = '{lesson_title}' and m.value = '{mark_value}'
            '''
    cursor.execute(select_query)
    data = cursor.fetchall()
    if len(data) > 0:
        print(
    f'Name: {name}, '
    f'Second name: {second_name}, '
    f'Book: {book_title}, '
    f'Subject: {subject_title}, '
    f'Lesson: {lesson_title}, '
    f'Mark: {mark_value}'
)
