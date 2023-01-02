import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE products (id INTEGER PRIMARY KEY, product_title TEXT NOT NULL, price REAL NOT NULL 
                DEFAULT 0.0, quantity INTEGER NOT NULL DEFAULT 0)''')


def add_product(product_title, price, quantity):
    cursor.execute('''INSERT INTO products(prctoduct_title, price, quantity) VALUES (?, ?, ?)''',
                   (product_title, price, quantity))
    conn.commit()


add_product('Ноутбук', 1000, 10)


def update_quantity(product_id, new_quantity):
    cursor.execute('''UPDATE products SET quantity = ? WHERE id = ?''', (new_quantity, product_id))
    conn.commit()


update_quantity(1, 20)

def update_price(product_id, new_price):
    cursor.execute('''UPDATE products SET price = ? WHERE id = ?''', (new_price, product_id))
    conn.commit()


update_price(1, 1500)


def delete_product(product_id):
    cursor.execute('''DELETE FROM products WHERE id = ?''', (product_id,))
    conn.commit()


delete_product(1)


def add_multiple_products():
    products = [
        ('Телефон', 2000, 5),
        ('Монитор', 1500, 10),
        ('Клавиатура', 500, 15),
        ('Мышь', 300, 20),
        ('Принтер', 1000, 25),
        ('Сканер', 800, 30),
        ('Наушники', 700, 35),
        ('Колонки', 600, 40),
        ('ТВ-бокс', 400, 45),
        ('Игровая консоль', 2000, 50),
        ('Игра', 600, 55),
        ('Картридж', 300, 60),
        ('Батарейки', 100, 65),
        ('Зарядное устройство', 200, 70),
        ('Чехол', 300, 75)
    ]
    cursor.executemany('''INSERT INTO products(product_title, price, quantity) VALUES (?, ?, ?)''', products)
    conn.commit()


add_multiple_products()


def get_all_products():
    cursor.execute('''SELECT * FROM products''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)


get_all_products()


def get_products_by_price(price):
    cursor.execute('''SELECT * FROM products WHERE price > ?''', (price,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)


get_products_by_price(1000)


def get_products_by_quantity(quantity):
    cursor.execute('''SELECT * FROM products WHERE quantity > ?''', (quantity,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)


get_products_by_quantity(50)


def sort_products_by_price():
    cursor.execute('''SELECT * FROM products ORDER BY price''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)


sort_products_by_price()


def sort_products_by_quantity():
    cursor.execute('''SELECT * FROM products ORDER BY quantity''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)


sort_products_by_quantity()


def delete_all_products():
    cursor.execute('''DELETE FROM products''')
    conn.commit()


delete_all_products()

conn.close()
