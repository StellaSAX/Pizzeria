import sqlite3

def fetch_guests_with_orders():
    """
    Получает список всех гостей с их заказами.

    :param db_name: Имя файла базы данных (по умолчанию 'pizza_database.db').
    :return: Список кортежей с информацией о гостях и их заказах.
    """
    # Создаем подключение к базе данных
    conn = sqlite3.connect('..\pizza_database.db')
    cursor = conn.cursor()

    # Запрос для получения списка всех гостей с их заказами
    query = '''
    SELECT Guest.Имя, Guest.Фамилия, Orders.Дата_заказа, Orders.Статус_заказа, Pizza.Название
    FROM Guest
    LEFT JOIN Orders ON Guest.id_Посетителя = Orders.id_Посетителя
    LEFT JOIN Pizza  ON Orders.id_Номер = Pizza.id_Номер
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
    print("Список гостей с их заказами:")
    for row in guests_with_Orderss:
        имя, фамилия, дата_заказа, статус, название = row
        print(f"Гость: {имя} {фамилия}, Заказ: {дата_заказа}, Статус: {статус}, Пицца: {название}")
