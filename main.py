import sqlite3

con = sqlite3.connect('new.db')
cur = con.cursor()

cur.executescript("""

INSERT INTO Student (name, surname, age, grade, rating) 
VALUES 
('Ali', 'Toshpoev', 20, 'A', 95),
('Zarina', 'Abdullaeva', 19, 'B', 88),
('Murod', 'Jumayev', 21, 'C', 75);


INSERT INTO Book (book_name, author, page)
VALUES 
('Mathematics for Beginners', 'John Smith', 250),
('Advanced Physics', 'Alex Brown', 320),
('Computer Science 101', 'Sophie Davis', 400);


INSERT INTO Teacher (name, surname, subject, book_id) 
VALUES 
('Dr. James', 'Wilson', 'Mathematics', 1),
('Prof. Maria', 'Taylor', 'Physics', 2),
('Dr. Emma', 'Clark', 'Computer Science', 3);


INSERT INTO School (ceo_name, school_rating, subject, student_id, book_id, teacher_id) 
VALUES 
('Olim Tursunov', 90, 'Mathematics', 1, 1, 1),
('Nilufar Akhmedova', 85, 'Physics', 2, 2, 2),
('Shahzoda Azizova', 80, 'Computer Science', 3, 3, 3);

""")

con.commit()
con.close()