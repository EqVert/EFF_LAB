class User:
    type_engineer = 1
    type_manager = 2

    def __init__(self, name, age, type, phone, phone_code):
        self.name = name
        self.age = age
        self.type = type
        self.phone = phone
        self.phone_code = phone_code

    def print_details(self):
        # Виведення інформації про користувача
        print("Name:", self.name)
        print("Age:", self.age)
        print("Type:", self.type)
        print("Phone:", self.phone_code + self.phone)

# Приклад використання класу
user = User("John", 25, User.type_engineer, "9379992", "050")
user.print_details()
