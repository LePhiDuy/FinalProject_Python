import os

from django.db import IntegrityError
from faker import Faker
import django

# Thiết lập biến môi trường DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CoffeeShop.settings")

# Cấu hình Django
django.setup()

from coffee.models import Category, Product

# Tạo một đối tượng Faker
fake = Faker()

# Tạo danh sách các loại cà phê
categories = [
    'Espresso', 'Cappuccino', 'Latte', 'Americano', 'Mocha'
]

# Tạo 5 Category
for cat_name in categories:
    cat = Category(name=cat_name, image=fake.image_url(), description=fake.text())
    cat.save()

    # Tạo 10 sản phẩm cho mỗi Category
    for i in range(10):
        product = Product(
            name=fake.text(max_nb_chars=50),
            price=fake.pyfloat(min_value=1, max_value=20, right_digits=2),
            quantity=fake.random_int(min=1, max=100),
            category_id=cat,
            image=fake.image_url()
        )
        try:
            product.save()
        except IntegrityError:
            # Đảm bảo rằng các sản phẩm có tên khác nhau
            pass
