


square_meters = float(input())

price_per_sm = 7.61
all_price = price_per_sm * square_meters
discount = all_price * 0.18
total_price = all_price - discount

print(f'The final price is: {total_price} lv.')
print(f'The discount is: {discount} lv')
