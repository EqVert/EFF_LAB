# 1. Інкапсулювати поля - змінити всі відкриті поля на приватні, додавши двокрапку "_" на початку їхніх назв:
class Product:
	def __init__(self, product_id, name, category, price):
		self._product_id = product_id
		self._name = name
		self._category = category
		self._price = price

# 2. Створити публічні методи для отримання та встановлення значень приватних полів:
class Product:
	def __init__(self, product_id, name, category, price):
		self._product_id = product_id
		self._name = name
		self._category = category
		self._price = price

	def get_product_id(self):
		return self._product_id

	def set_product_id(self, product_id):
		self._product_id = product_id

	def get_name(self):
		return self._name

	def set_name(self, name):
		self._name = name

	def get_category(self):
		return self._category

	def set_category(self, category):
		self._category = category

	def get_price(self):
		return self._price

	def set_price(self, price):
		self._price = price
# 3. Замість відкритого доступу до полів класу Product через self.products, можно додати методи для отримання та оновлення продуктів:
class InventoryManagement:
	def __init__(self, products):
		self._products = products

	def get_products(self):
		return self._products

	def add_product(self, product):
		self._products.append(product)

	def remove_product(self, product):
		self._products.remove(product)

# 4. Замінити прямий доступ до полів Product на виклики відповідних геттерів:
def print_product_details(self, product_id):
	for product in self.get_products():
		if product.get_product_id() == product_id:
			print(f"Product ID: {product.get_product_id()}, Name: {product.get_name()}, Category: {product.get_category()}, Price: {product.get_price()}")