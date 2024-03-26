class ShapeCalculator:
	def __init__(self):
		self.area_calculators = {
			"circle": self.calculate_circle_area,
			"rectangle": self.calculate_rectangle_area,
			"triangle": self.calculate_triangle_area
		}

	def calculate_area(self, shape_type):
		calculator = self.area_calculators.get(shape_type)
		if calculator:
			calculator()
		else:
			print("Unknown shape type:", shape_type)

	def calculate_circle_area(self):
		radius = float(input("Enter the radius of the circle: "))
		area = 3.14 * radius * radius
		print("Area:", area)

	def calculate_rectangle_area(self):
		length = float(input("Enter the length of the rectangle: "))
		width = float(input("Enter the width of the rectangle: "))
		area = length * width
		print("Area:", area)

	def calculate_triangle_area(self):
		base = float(input("Enter the base of the triangle: "))
		height = float(input("Enter the height of the triangle: "))
		area = 0.5 * base * height
		print("Area:", area)

# Приклад використання класу
calculator = ShapeCalculator()
calculator.calculate_area("circle")
