PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3.00
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2.00

vacation_coast = float(input())
puzzle_count = int(input())
talking_doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

total_count = puzzle_count + talking_doll_count + teddy_bear_count + minion_count + truck_count

discount = 0
if total_count >= 50:
    discount = 0.25

total_income = puzzle_count * PUZZLE_PRICE \
               + talking_doll_count * TALKING_DOLL_PRICE \
               + teddy_bear_count * TEDDY_BEAR_PRICE \
               + minion_count * MINION_PRICE \
               + truck_count + TRUCK_PRICE

total_income_with_discount = total_income * (1 - discount)

rent_coast = total_income_with_discount * 0.10

final_income = total_income_with_discount - rent_coast

if final_income >= vacation_coast:
    print (f"Yes! {final_income - vacation_coast:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_coast - final_income:.2f} lv needed.")

# excursion_price = float(input())
# puzzles_count = int(input())
# dolls_count = int(input())
# teddy_bears_count = int(input())
# minions_count = int(input())
# trucks_count = int(input())
#
# puzzles_price = puzzles_count * 2.60
# dolls_price = dolls_count * 3.00
# teddy_bears_price = teddy_bears_count * 4.10
# minions_price = minions_count * 8.20
# trucks_price = trucks_count * 2.00
#
# total_price = puzzles_price + dolls_price + teddy_bears_price + minions_price + trucks_price
#
# if puzzles_count + dolls_count + teddy_bears_count + minions_count + trucks_count >= 50:
#     total_price *= 0.75
#
# total_price *= 0.9
# remaining_money = abs(excursion_price - total_price)
#
# if total_price >= excursion_price:
#     print(f"Yes! {remaining_money:.2f} lv left.")
# else:
#     print(f"Not enough money! {remaining_money:.2f} lv needed.")