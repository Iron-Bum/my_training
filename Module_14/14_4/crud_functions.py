import sqlite3 as sq


def initiate_db():
    connection = sq.Connection('products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    ) 
    ''')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_title ON Products (title)')
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
