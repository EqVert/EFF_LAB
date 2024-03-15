function sumEvenNumbers(data) {
  let sum = 0
  for (let i = 0; i < data.length; i++) {
    let element = data[i]
    if (element % 2 === 0) {
      sum += element
    }
  }
  return sum
}

// Приклад використання
let sum = sumEvenNumbers([1, 2, 3, 4, 5, 6, 'seven', 8, 9, 10])
console.log(`Сума четних чисел: ${sum}`)