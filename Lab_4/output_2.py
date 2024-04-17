class Shape:
  def area(self, side=None, radius=None):
    if side is not None:
      return side ** 2
    elif radius is not None:
      return 3.14 * radius ** 2
    else:
      raise ValueError("No valid parameter")

class Square(Shape):
  def area(self, side):
    return super().area(side=side)

class Circle(Shape):
  def area(self, radius):
    return super().area(radius=radius)

# Приклад використання класів
square = Square()
print("Area of square:", square.area(5))
circle = Circle()
print("Area of circle:", circle.area(3))
