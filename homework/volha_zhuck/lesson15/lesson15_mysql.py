import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
cursor.execute(
    "INSERT INTO students (name, second_name) VALUES ('Fredrick', 'Backman')"
)

student_id = cursor.lastrowid
insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('My Grandmother asked me..', student_id),
        ('A Man called Ove', student_id),
        ('Britt-Marie', student_id)
    ]
)

cursor.execute(
    "INSERT INTO `st-onl`.groups (title, start_date, end_date) "
    "VALUES ('Swedish', 'October-24', 'November-24')"
)

group_id = cursor.lastrowid
cursor.execute(
    "UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id)
)

cursor.execute("INSERT INTO subjets (title) VALUES ('Reading')")
reading_id = cursor.lastrowid
cursor.execute("INSERT INTO subjets (title) VALUES ('Writing')")
writing_id = cursor.lastrowid
cursor.execute(
    "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ('Writing Lesson 1', writing_id)
)

w_lesson1_id = cursor.lastrowid
cursor.execute(
    "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ('Writing Lesson 2', writing_id)
)

w_lesson2_id = cursor.lastrowid
cursor.execute(
    "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ('Reading Lesson 1', reading_id)
)

r_lesson1_id = cursor.lastrowid
cursor.execute(
    "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ('Reading Lesson 2', reading_id)
)

r_lesson2_id = cursor.lastrowid
insert_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query, [
        ('7', r_lesson1_id, student_id),
        ('8', r_lesson2_id, student_id),
        ('3', w_lesson1_id, student_id),
        ('9', w_lesson2_id, student_id)

    ]
)

cursor.execute(f'SELECT * from students where id = {student_id}')
print(cursor.fetchone())
cursor.execute(f'SELECT title FROM books where taken_by_student_id ={student_id}')
print(cursor.fetchall())
select_query = '''
SELECT *
FROM students s
left JOIN books b ON b.taken_by_student_id = s.id
left JOIN marks m ON m.student_id = s.id
left join lessons l ON l.id = m.lesson_id
left join subjets sub ON sub.id = l.subject_id
left JOIN `st-onl`.groups on `st-onl`.groups.id = s.group_id
WHERE s.id = %s
'''
cursor.execute(select_query, (student_id,))
print(cursor.fetchall())
db.commit()
db.close()
