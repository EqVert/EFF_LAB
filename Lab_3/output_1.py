class Shape:
	def calculate_area(self):
		pass

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def calculate_area(self):
		area = 3.14 * self.radius ** 2
		print("Area of the circle:", area)

class Rectangle(Shape):
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def calculate_area(self):
		area = self.length * self.width
		print("Area of the rectangle:", area)

class Triangle(Shape):
	def __init__(self, base, height):
		self.base = base
		self.height = height

	def calculate_area(self):
		area = 0.5 * self.base * self.height
		print("Area of the triangle:", area)

def create_shape(shape_type):
	if shape_type == "circle":
		radius = float(input("Enter the radius of the circle: "))
		return Circle(radius)
	elif shape_type == "rectangle":
		length = float(input("Enter the length of the rectangle: "))
		width = float(input("Enter the width of the rectangle: "))
		return Rectangle(length, width)
	elif shape_type == "triangle":
		base = float(input("Enter the base of the triangle: "))
		height = float(input("Enter the height of the triangle: "))
		return Triangle(base, height)
	else:
		return None
# Приклад виклику програми
shape_type = input("Enter the type of shape (circle, rectangle, triangle): ")
shape = create_shape(shape_type)

if shape:
	shape.calculate_area()
else:
	print("Invalid shape type")
