import sqlite3

con = sqlite3.connect('new.db')
cur = con.cursor()

cur.executescript("""

SELECT s.name, s.surname, b.book_name
FROM Student s
JOIN Book b ON s.student_id = b.book_id
WHERE s.rating > (SELECT AVG(rating) FROM Student);

""")

con.commit()
con.close()