class Shape:
	def __init__(self, shape_type):
		self.shape_type = shape_type

	def calculate_area(self):
		area = 0
		if self.shape_type == "circle":
			radius = float(input("Enter the radius of the circle: "))
			area = 3.14 * radius * radius
		elif self.shape_type == "rectangle":
			length = float(input("Enter the length of the rectangle: "))
			width = float(input("Enter the width of the rectangle: "))
			area = length * width
		elif self.shape_type == "triangle":
			base = float(input("Enter the base of the triangle: "))
			height = float(input("Enter the height of the triangle: "))
			area = 0.5 * base * height
		print("Area:", area)

# Приклад виклику програми
shape_type = input("Enter the type of shape (circle, rectangle, triangle): ")
shape = Shape(shape_type)
shape.calculate_area()