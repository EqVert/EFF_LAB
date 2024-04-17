class Product:
  def __init__(self, name, price, type):
    self.name = name
    self.price = price
    self.type = type

class ProductSearch:
  def search_product(self, query):
    # Пошук продукту
    pass

class ProductDisplay:
  def display_product(self, product):
    # Відображення деталей продукту
    print(f"Product: {product.name}, Price: {product.price}, Type: {product.type}")

class ProductOrder:
  def order_product(self, product, quantity):
    # Процес замовлення
    print(f"Ordered {quantity} of {product.name}")

# Приклад використання: 
# Створення продукту
prod = Product("Apple", 10, "Fruit")

# Пошук продуктів
searcher = ProductSearch()
searcher.search_product("Apple")

# Відображення продукту
displayer = ProductDisplay()
displayer.display_product(prod)

# Замовлення продукту
orderer = ProductOrder()
orderer.order_product(prod, 5)
