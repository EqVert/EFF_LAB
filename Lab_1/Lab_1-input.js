class DataArray {
  constructor(data) {
    this.data = data
  }

  // Метод для перевірки, чи є елемент масиву числом
  isNumber(element) {
    return typeof element === 'number' && !isNaN(element)
  }

  // Метод для перевірки, чи є число парним
  isEven(number) {
    return number % 2 === 0
  }

  // Метод для підрахунку суми парних чисел
  sumEvenNumbers() {
    let sum = 0
    for (let i = 0; i < this.data.length; i++) {
      let element = this.data[i]
      // Перевіряємо, чи є елемент числом
      if (this.isNumber(element)) {
        // Перевіряємо, чи є число парним
        if (this.isEven(element)) {
          sum += element
        }
      } else {
        // Виводимо попередження, якщо елемент не є числом
        console.warn(`Элемент ${element} не является числом`)
      }
    }
    return sum
  }
}

// Приклад використання
let dataArray = new DataArray([1, 2, 3, 4, 5, 6, 'seven', 8, 9, 10])
let sum = dataArray.sumEvenNumbers()
console.log(`Сумма четных чисел: ${sum}`)