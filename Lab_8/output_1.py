# 1. Переміщення методу calculate_shipping_cost у клас Customer:
class Customer:
	def __init__(self, name, address):
		self.name = name
		self.address = address

	def get_address(self):
		return self.address

	def calculate_shipping_cost(self):
		address = self.address
		if "New York" in address:
			return 5.00
		elif "California" in address:
			return 10.00
		else:
			return 15.00

# 2. Тепер, коли метод calculate_shipping_cost переміщено до класу Customer,
# 		ми можемо викликати його з екземпляра Customer у методі print_order_details.
class Order:
	def __init__(self, customer, product, quantity):
		self.customer = customer
		self.product = product
		self.quantity = quantity

	def print_order_details(self):
		print(f"Order for {self.product} x {self.quantity}")
		print(f"Shipping to {self.customer.get_address()}")
		shipping_cost = self.customer.calculate_shipping_cost()
		print(f"Shipping cost: ${shipping_cost:.2f}")

# Цей рефакторинг допоможе зменшити дублювання коду та покращити організацію коду,
# оскільки методи, пов'язані з даними, тепер знаходяться у тому ж класі, що і самі дані.