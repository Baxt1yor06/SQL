import sqlite3

con = sqlite3.connect('new.db')
cur = con.cursor()

cur.executescript("""
CREATE TABLE IF NOT EXISTS Student (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    surname VARCHAR(50),
    age INTEGER,
    grade VARCHAR(50),
    rating INTEGER
);

CREATE TABLE IF NOT EXISTS Book(
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_name VARCHAR(50),
    author VARCHAR(50),
    page INTEGER
);

CREATE TABLE IF NOT EXISTS Teacher(
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    surname VARCHAR(50),
    subject VARCHAR(50),
    book_id INTEGER,
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

CREATE TABLE IF NOT EXISTS School(
    school_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ceo_name VARCHAR(50),
    school_rating INTEGER,
    subject VARCHAR(50),
    student_id INTEGER,
    book_id INTEGER,
    teacher_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
);
""")

con.commit()
con.close()
