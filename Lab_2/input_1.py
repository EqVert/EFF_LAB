def calculate_score(name, age, gender, height, weight, score1, score2, score3, score4, score5):
    # Бізнес-логіка для розрахунку загального рейтингу
    total_score = score1 + score2 + score3 + score4 + score5

    # Перевірка чи користувач є повнолітнім
    is_adult = True if age >= 18 else False

    # Виведення результатів
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Height:", height)
    print("Weight:", weight)
    print("Total Score:", total_score)
    print("Adult:", is_adult)

# Приклад виклику функції
calculate_score("John", 25, "Male", 175, 70, 85, 90, 75, 88, 92)
