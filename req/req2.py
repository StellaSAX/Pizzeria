import sqlite3

def fetch_all_data():
    """
    Получает все данные из таблиц Guest, Orders, Pizzerias и Pizzas.

    :return: Словарь с данными из всех таблиц.
    """

    conn = sqlite3.connect('..\pizza_database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Guest')
    guests = cursor.fetchall() 

    cursor.execute('SELECT * FROM Orders')
    orders = cursor.fetchall()  

    cursor.execute('SELECT * FROM Pizzeria')
    pizzerias = cursor.fetchall()  

    cursor.execute('SELECT * FROM Pizza')
    pizzas = cursor.fetchall() 

    # Закрываем соединение
    conn.close()

    return {
        "guests": guests,
        "orders": orders,
        "pizzerias": pizzerias,
        "pizzas": pizzas
    }

# Пример использования функции
if __name__ == "__main__":
    data = fetch_all_data()

    print("Гости:")
    for guest in data["guests"]:
        print(guest)

    print("\nЗаказы:")
    for orders in data["orders"]:
        print(booking)

    print("\nПиццерии:")
    for pizzerias in data["pizzerias"]:
        print(hotel)

    print("\nПиццы:")
    for pizzas in data["pizzas"]:
        print(room)
