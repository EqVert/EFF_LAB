## calculate_base_total_price керує обчисленням загальної вартості
## з урахуванням або без урахування знижки

def calculate_base_total_price(product_prices, discount):
  total_price = 0
  for price in product_prices:
    if discount:
      total_price += price * 0.9
    else:
      total_price += price
  return total_price

def calculate_total_price(product_prices, discount):
  return calculate_base_total_price(product_prices, discount)

def calculate_total_price_with_tax(product_prices, discount, tax_rate):
  total_price = calculate_base_total_price(product_prices, discount)
  total_price *= (1 + tax_rate)
  return total_price