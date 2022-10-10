import sqlite3

conn = sqlite3.connect('hw.sqlite3')
cur = conn.cursor()


def load_users() -> tuple:
    with open('users.txt', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    for i in range(len(lines)):
        lines[i] = lines[i].split('~')
    lines = tuple(map(tuple, lines))

    return lines

load_users()

def load_statues() -> tuple:
    with open('statuses', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    for i in range(len(lines)):
        lines[i] = lines[i].split('\n')
    lines = tuple(map(tuple, lines))

    return lines

load_statues()

def load_orders() -> tuple:
    with open('orders', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    for i in range(len(lines)):
        lines[i] = lines[i].split('~')
    lines = tuple(map(tuple, lines))

    return lines

load_orders()

def load_order_items() -> tuple:
    with open('order_items', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    for i in range(len(lines)):
        lines[i] = lines[i].split('-')
    lines = tuple(map(tuple, lines))

    return lines

load_order_items()

def load_categories() -> tuple:
    with open('categories', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    for i in range(len(lines)):
        lines[i] = lines[i].split('-')
    lines = tuple(map(tuple, lines))

    return lines

load_categories()

def load_products() -> tuple:
    with open('products', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    for i in range(len(lines)):
        lines[i] = lines[i].split('~')
    lines = tuple(map(tuple, lines))

    return lines

load_products()

def create_table() -> None:
    cur.execute('''
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        status_id INTEGER
    );
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS order_items(
        id INTEGER PRIMARY KEY,
        order_id INTEGER, 
        product_id INTEGER, 
        FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE,
        FOREIGN KEY (product_id) REFERENCES product (id) ON DELETE CASCADE
    );
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY,
        title VARCHAR(36),
        description VARCHAR(140),
        category_id INTEGER, 
        FOREIGN KEY (category_id) REFERENCES category (id) ON DELETE CASCADE
    );
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY,
        name VARCHAR(24) UNIQUE
    );
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name VARCHAR(24),
        email VARCHAR(24) UNIQUE
    );
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS statuses(
        id INTEGER PRIMARY KEY,
        name VARCHAR(10) UNIQUE
    );
    ''')

    conn.commit()


create_table()

def fill_users(users: tuple) -> None:
    for user in users:
        cur.execute('''
        INSERT INTO users(
        name, email) VALUES(?, ?);
        ''', user)
        conn.commit()

fill_users(load_users())

def fill_statuses(statuses: tuple) -> None:
    for status in statuses:
        cur.execute('''
        INSERT INTO statuses(name) 
        VALUES(?);
        ''', status)
        conn.commit()

fill_statuses(load_statues())

def fill_orders(orders: tuple) -> None:
    for order in orders:
        cur.execute('''
        INSERT INTO orders (user_id, status_id)
        VALUES (?, ?);
        ''', order)
        conn.commit()

fill_orders(load_orders())

def fill_order_items(order_items: tuple) -> None:
    for items in order_items:
        cur.execute('''
        INSERT INTO order_items (order_id, product_id)
        VALUES (?, ?);
        ''', items)
        conn.commit()

fill_order_items(load_order_items())

def fill_categories(categories: tuple) -> None:
    for category in categories:
        cur.execute('''
        INSERT INTO categories (name)
        VALUES (?);
        ''', category)
        conn.commit()

fill_categories(load_categories())

def fill_products(products: tuple) -> None:
    for product in products:
        cur.execute('''
        INSERT INTO products (title, description, category_id)
        VALUES (?, ?, ?);
        ''', product)
        conn.commit()

fill_products(load_products())


cur.execute('''
SELECT * FROM users;
''')
print(cur.fetchall())

cur.execute('''
SELECT name, email FROM users, orders WHERE users.id=user_id;
''')
print(cur.fetchall())