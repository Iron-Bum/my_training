import sqlite3 as sq

connection = sq.Connection('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL        
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

for i in range(1, 11):
    cursor.execute(
        'INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)', (
            f'User{i}', f'example{i}@gmail.com', f'{i}0', '1000'
        )
    )

cursor.execute('''
UPDATE Users
SET balance = 500
WHERE id IN (
    SELECT id FROM (
        SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS rn
        FROM Users
    ) WHERE rn % 2 != 0
)
''')

cursor.execute('''
DELETE FROM Users
WHERE id IN (
    SELECT id FROM (
        SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS rn
        FROM Users
    ) WHERE rn % 3 = 1
)
''')

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
rows = cursor.fetchall()

for row in rows:
    username, email, age, balance = row
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

connection.commit()
connection.close()
