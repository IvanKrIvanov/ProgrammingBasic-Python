# # # Първи ред – джобните на Тереза на ден – реално число в интервала [1.00 ...100.00]
# # #  Втори ред – парите, които тя печели на ден от продажби – реално число в интервала [1.00...1000.00]
# # #  Трети ред – разходите на Тереза за целия период – реално число в интервала [1.00...1000.00]
# # # #  Четвърти ред – цената на подаръка – реално число в интервала [1.00...10000.00]
# # #
# # tereza_money = float(input())
# # sales_money = float(input())
# # expense_money = float(input())
# # price_present = float(input())
# #
# # saved_money = ((tereza_money * 5) + (sales_money * 5)) - expense_money
# # if saved_money > price_present:
# #     print(f"Profit: {saved_money:.2f} BGN, the gift has been purchased.")
# # else:
# #     print(f"Insufficient money: {saved_money:.2f} BGN.")
# #
#
# tereza_money = float(input())
# sales_money = float(input())
# expense_money = float(input())
# price_present = float(input())
#
# saved_money = ((tereza_money + sales_money) * 5) - expense_money
#
# if saved_money > price_present:
#     print(f"Profit: {saved_money:.2f} BGN, the gift has been purchased.")
# else:
#     print(f"Insufficient money: {saved_money:.2f} BGN.")
#

pocket_money_per_day = float(input())
earnings_per_day = float(input())
expenses = float(input())
gift_price = float(input())

total_savings = pocket_money_per_day * 5 + earnings_per_day * 5
total_savings -= expenses

if total_savings >= gift_price:
    print(f"Profit: {total_savings:.2f} BGN, the gift has been purchased.")
else:
    insufficient_money = gift_price - total_savings
    print(f"Insufficient money: {insufficient_money:.2f} BGN.")

