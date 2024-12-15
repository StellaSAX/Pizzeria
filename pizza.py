from sqlmodel import SQLModel, Field, Relationship, Session, create_engine, select
from typing import List, Optional
from sqlalchemy import text
from uuid import uuid4

class Pizza(SQLModel, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    name: str
    price: float

class Customer(SQLModel, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    name: str
    email: str

class PizzaOrder(SQLModel, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    pizza_id: int = Field(foreign_key="pizza.id")
    quantity: int
    payments: List["Payment"] = Relationship(back_populates="order")

class Employee(SQLModel, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    name: str
    position: str
    salary: float

class Payment(SQLModel, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    order_id: int = Field(foreign_key="pizzaorder.id")
    amount: float
    payment_date: str  # Можно использовать тип datetime для более точного хранения
    order: PizzaOrder = Relationship(back_populates="payments")

# Создаем базу данных
engine = create_engine("sqlite:///pizzeria.db")
SQLModel.metadata.create_all(engine)

# Заполняем базу данных
with Session(engine) as session:
    # Добавляем пиццы
    pizza1 = Pizza(name="Маргарита", price=8.50)
    pizza2 = Pizza(name="Пепперони", price=9.00)
    session.add(pizza1)
    session.add(pizza2)

    # Добавляем клиентов
    customer1 = Customer(name="Иван Иванов", email="ivan@example.com")
    customer2 = Customer(name="Мария Петрова", email="maria@example.com")
    session.add(customer1)
    session.add(customer2)

    # Добавляем заказы
    order1 = PizzaOrder(customer_id=1, pizza_id=1, quantity=2)
    order2 = PizzaOrder(customer_id=2, pizza_id=2, quantity=1)
    session.add(order1)
    session.add(order2)

    # Создаем сотрудников
    employee1 = Employee(name="Алексей Смирнов", position="Повар", salary=30000)
    employee2 = Employee(name="Ольга Кузнецова", position="Официант", salary=25000)
    session.add(employee1)
    session.add(employee2)
    
    # Создаем платежи
    payment1 = Payment(order_id=order1.id, amount=17.00, payment_date="2024-12-15")
    payment2 = Payment(order_id=order2.id, amount=9.00, payment_date="2024-12-15")
    session.add(payment1)
    session.add(payment2)
    
    session.commit()

def get_orders_with_details(session: Session):
    query = text(
        "SELECT c.name AS customer_name, p.name AS pizza_name,"
        "'Кол-во: ' as MESSAGE, o.quantity "
        "FROM PizzaOrder o "
        "JOIN Customer c ON o.customer_id = c.id "
        "JOIN Pizza p ON o.pizza_id = p.id"
    )
    orders = session.execute(query).all()
    return orders

def get_all_employees(session: Session):
    return session.query(Employee).all()

def get_all_payments(session: Session):
    return session.query(Payment).all()

# Использование метода
with Session(engine) as session:
    
    orders = get_orders_with_details(session)
    for order in orders:
        print(order)
        
    employees = get_all_employees(session)
    payments = get_all_payments(session)
    
    print("Сотрудники:")
    for employee in employees:
        print(f"{employee.name} - {employee.position} - {employee.salary} руб.")
    
    print("\nПлатежи:")
    for payment in payments:
        print(f"Платеж {payment.id}: {payment.amount} руб. за заказ {payment.order_id} на дату {payment.payment_date}")
