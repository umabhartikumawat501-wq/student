import sqlite3


def get_connection():
    connection = sqlite3.connect("students.db")
    return connection


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject TEXT,
            marks REAL,
            credits REAL
        )
    """)

    connection.commit()
    connection.close()


def get_marks(student_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, subject, marks, credits
        FROM marks
        WHERE student_id = ?
    """, (student_id,))

    marks = cursor.fetchall()

    connection.close()

    return marks


def delete_marks(mark_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM marks WHERE id = ?",
        (mark_id,)
    )

    connection.commit()
    connection.close()


def add_marks(student_id, subject, marks, credits):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO marks (student_id, subject, marks, credits)
        VALUES (?, ?, ?, ?)
    """, (student_id, subject, marks, credits))

    connection.commit()
    connection.close()