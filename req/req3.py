import sqlite3

def fetch_guests_with_orders():
    """
    Получает список всех заказов из пиццерий.
    """
    # Создаем подключение к базе данных
    conn = sqlite3.connect('..\pizza_database.db')
    cursor = conn.cursor()

    # Запрос для получения списка всех гостей с их заказами
    query = '''
    SELECT Pizzeria.Название, Orders.Дата_заказа, Orders.Статус_заказа, Pizza.Название
    FROM Pizzeria
    LEFT JOIN Pizza  ON Pizzeria.id_Пиццерии = Pizza.id_Пиццерии
    LEFT JOIN Orders ON Pizza.id_Номер = Orders.id_Номер
    '''

    # Выполнение запроса
    cursor.execute(query)

    # Получение результатов
    results = cursor.fetchall()

    # Закрываем соединение
    conn.close()

    return results

# Пример использования функции
if __name__ == "__main__":
    guests_with_Orderss = fetch_guests_with_orders()

    # Вывод результатов
    print("Список Заказов из Пиццерий:")
    for row in guests_with_Orderss:
        название_места, дата_заказа, статус, название = row
        print(f"Пиццерия: {название_места}, Заказ: {дата_заказа}, Статус: {статус}, Пицца: {название}")
