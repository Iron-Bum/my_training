import sqlite3 as sq


def initiate_db():
    connection = sq.Connection('products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    ) 
    ''')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_title ON Products (title)')
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS Users (
       id INTEGER PRIMARY KEY,
       username TEXT NOT NULL,
       email TEXT NOT NULL,
       age INT NOT NULL,
       balance INT NOT NULL
       ) 
       ''')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
    connection.commit()
    connection.close()


def add_products():
    connection = sq.Connection('products.db')
    cursor = connection.cursor()
    for i in range(1, 5):
        cursor.execute(
            'INSERT INTO Products(title, description, price) VALUES(?, ?, ?)', (
                f'Продукт {i}', f'Описание {i}', f'{i}00'
            )
        )
    connection.commit()
    connection.close()


def get_all_products():
    connection = sq.Connection('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT title, description, price FROM Products')
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result


def is_included(username):
    connection = sq.Connection('products.db')
    cursor = connection.cursor()
    users_list = cursor.execute('SELECT username FROM Users').fetchall()
    usernames = [user[0] for user in users_list]
    connection.close()
    return username in usernames


def add_user(username, email, age):
    connection = sq.Connection('products.db')
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)', (
            username, email, age, 1000
        )
    )
    connection.commit()
    connection.close()