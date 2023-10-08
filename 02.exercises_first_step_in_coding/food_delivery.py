
# Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
# Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).
# Цената на доставка е 2.50 лв и се начислява най-накрая.

CHIKEN_MENU = 10.35
FISH_MENU = 12.40
VEGGE_MENU = 8.15
DELIVERY = 2.50

chiken_menu_amounts = int(input())
fish_menu_amounts = int(input())
vegge_menu_amounts = int(input())

total_price_menu = (chiken_menu_amounts * CHIKEN_MENU) \
                   + (fish_menu_amounts * FISH_MENU) \
                   + (vegge_menu_amounts * VEGGE_MENU)

desert = total_price_menu * 0.2

final_price = total_price_menu + desert + DELIVERY
print(final_price)
