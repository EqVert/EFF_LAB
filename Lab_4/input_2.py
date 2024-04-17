class Square:
  def area_square(self, side):
    return side ** 2

class Circle:
  def area_circle(self, radius):
    return 3.14 * radius ** 2

# Приклад використання класів
square = Square()
print("Area of square:", square.area_square(5))
circle = Circle()
print("Area of circle:", circle.area_circle(3))
