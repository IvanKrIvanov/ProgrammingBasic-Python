budget = float(input())
num_graphics_cards = int(input())
num_processors = int(input())
num_ram = int(input())

graphics_cards_price = num_graphics_cards * 250
processors_price = num_processors * (graphics_cards_price * 0.35)
ram_price = num_ram * (graphics_cards_price * 0.1)

total_price = graphics_cards_price + processors_price + ram_price
if num_graphics_cards > num_processors:
    total_price *= 0.85

if budget >= total_price:
    remaining_budget = budget - total_price
    print(f"You have {remaining_budget:.2f} leva left!")
else:
    needed_money = total_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")
