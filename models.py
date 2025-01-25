# Создание книги
new_book = Book(
    title="1984",
    author="George Orwell",
    category="Dystopia",
    year=1949,
    price=15.99,
    rental_price=5.99,
    status="available"
)
db.session.add(new_book)
db.session.commit()

# Создание пользователя
new_user = User(name="John Doe", email="john@example.com")
new_user.set_password("password123")
db.session.add(new_user)
db.session.commit()

# Создание заказа
new_order = Order(
    user_id=new_user.id,
    book_id=new_book.id,
    order_type="rental",
    end_date=datetime(2023, 12, 31)  # Пример даты окончания аренды
)
db.session.add(new_order)
db.session.commit()