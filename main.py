import sqlite3

conn = sqlite3.connect('mydatabase.db')
sql = conn.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, '
            'grade TEXT);')


# sql.execute('INSERT INTO students (name,age,grade) VALUES ("Arman",17,"D")')
# conn.commit()
# conn.close()

# students = sql.execute("SELECT * FROM students")
# print(students.fetchall())


def get_student_by_name(name):
    conn = sqlite3.connect('mydatabase.db')
    sql = conn.cursor()

    result = sql.execute("SELECT * FROM students WHERE name=?;", (name,)).fetchone()

    return result


# print(get_student_by_name("Liana"))

def update_student_grade(name, new_grade):
    conn = sqlite3.connect('mydatabase.db')
    sql = conn.cursor()

    sql.execute('UPDATE students SET grade=? WHERE name=?;', (new_grade, name))
    conn.commit()
    conn.close()

    return "Оценка успешно обновлена"


# print(update_student_grade('Liana', 'B'))

def delete_student(name):
    conn = sqlite3.connect('mydatabase.db')
    sql = conn.cursor()

    sql.execute('DELETE FROM students WHERE name=?', (name,))
    conn.commit()
    conn.close()
    return 'Запись студента успешно удалена из базы данных'


# print(delete_student('Kamron'))
