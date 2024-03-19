class Person:
    def __init__(self, name, age, gender, height, weight, scores):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.scores = scores

    def calculate_score(self):
        total_score = sum(self.scores)
        is_adult = True if self.age >= 18 else False

        # Виведення результатів
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Height:", self.height)
        print("Weight:", self.weight)
        print("Total Score:", total_score)
        print("Adult:", is_adult)

# Приклад виклику методу
person = Person("John", 25, "Male", 175, 70, [85, 90, 75, 88, 92])
person.calculate_score()
