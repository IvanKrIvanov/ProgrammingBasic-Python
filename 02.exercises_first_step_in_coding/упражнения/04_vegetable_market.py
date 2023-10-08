vegetable_price = float(input())
fruit_price = float(input())
vegetable_kg = int(input())
fruit_kg = int(input())

euro = 1.94

total_price_vegetable = vegetable_price * vegetable_kg
total_price_fruit = fruit_price * fruit_kg
total_price = (total_price_fruit + total_price_vegetable) / euro
print(f'{total_price:.2f}')