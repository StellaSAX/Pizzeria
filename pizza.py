import sqlite3

# Создаем подключение к базе данных (если базы данных нет, она будет создана)
conn = sqlite3.connect('pizza_database.db')

# Создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Создаем таблицу Посетители
cursor.execute('''
CREATE TABLE IF NOT EXISTS Guest (
    id_Посетителя INTEGER NOT NULL PRIMARY KEY,
    Имя TEXT DEFAULT '50',
    Фамилия TEXT DEFAULT '50',
    Номер_телефона TEXT DEFAULT '15',
    Email TEXT DEFAULT '100'
)
''')

# Заполнение таблицы Гости
guests = [
    (1, 'Иван', 'Иванов', '1234567890', 'ivan@example.com'),
    (2, 'Петр', 'Петров', '0987654321', 'petr@example.com'),
    (3, 'Светлана', 'Сидорова', '1122334455', 'svetlana@example.com')
]

cursor.executemany('''
INSERT INTO Guest (id_Посетителя, Имя, Фамилия, Номер_телефона, Email)
VALUES (?, ?, ?, ?, ?)
''', guests)

# Создаем таблицу Заказoв
cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    id_Заказа INTEGER NOT NULL PRIMARY KEY,
    id_Номер INTEGER,
    id_Посетителя INTEGER,
    Дата_заказа DATE,
    Статус_заказа TEXT DEFAULT '20',
    FOREIGN KEY (id_Номер) REFERENCES Меню(id_Номер),
    FOREIGN KEY (id_Посетителя) REFERENCES Гости(id_Посетителя)
)
''')

# Заполнение таблицы Заказoв
orderst = [
    (1, 101, 1, '2024-12-20', 'Подтверждено'),
    (2, 102, 2, '2024-12-22', 'Ожидает подтверждения'),
    (3, 103, 3, '2024-12-24', 'Отменено'),
    (4, 101, 2, '2024-12-27', 'Подтверждено'),
]

cursor.executemany('''
INSERT INTO Orders (id_Заказа, id_Номер, id_Посетителя, Дата_заказа, Статус_заказа)
VALUES (?, ?, ?, ?, ?)
''', orderst)

# Создаем таблицу Пицеррий
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pizzeria (
    id_Пиццерии INTEGER NOT NULL PRIMARY KEY,
    Название TEXT DEFAULT '50',
    Адрес TEXT DEFAULT '20',
    Номер_телефона TEXT DEFAULT '15',
    Общее_количество_блюд INTEGER NOT NULL,
    Дополнительная_информация TEXT
)
''')

# Заполнение таблицы Пицеррий
Pizzerias = [
    (1, 'Mamma Mia', 'Улица Солнечная, 1', '123456789', 50, 'Бесплатный Wi-Fi'),
    (2, 'Luigi&Mario', 'Улица Лунная, 2', '987654321', 30, 'Тук-тук')
]

cursor.executemany('''
INSERT INTO Pizzeria (id_Пиццерии, Название, Адрес, Номер_телефона, Общее_количество_блюд, Дополнительная_информация)
VALUES (?, ?, ?, ?, ?, ?)
''', Pizzerias)


# Создаем таблицу Меню
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pizza (
    id_Номер INTEGER NOT NULL PRIMARY KEY,
    id_гос INTEGER,
    id_Пиццерии INTEGER,
    Название TEXT DEFAULT '50',
    Цена DECIMAL(18, 0),
    Дополнительная_информация TEXT,
    FOREIGN KEY (id_гос) REFERENCES Номера(id_Номер),
    FOREIGN KEY (id_Пиццерии) REFERENCES Пиццерии(id_Пиццерии)
)
''')

# Заполнение таблицы Меню
pizzas = [
    (101, None, 1, 'Пепперони', 300, 'Пепперони за отдельную плату'),
    (102, None, 1, 'Четыре Сыра', 600, 'Пятый сыр в подарок'),
    (103, None, 2, 'Дьябло', 200, 'Запивать - святой водой')
]

cursor.executemany('''
INSERT INTO Pizza (id_Номер, id_гос, id_Пиццерии, Название, Цена, Дополнительная_информация)
VALUES (?, ?, ?, ?, ?, ?)
''', pizzas)

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
