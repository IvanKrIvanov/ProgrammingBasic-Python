deposit_amount = float(input())
deposit_months = int(input())
year_rate = float(input()) / 100

final_amount = deposit_amount + deposit_months * ((deposit_amount * year_rate) / 12)

print(final_amount)