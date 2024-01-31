dancers = int(input())
points = float(input())
season = input()
location = input()

if location == "Bulgaria":
    if season == "summer":
        expenses_percentage = 5
    else:
        expenses_percentage = 8
    winnings = dancers * points
else:
    if season == "summer":
        expenses_percentage = 10
    else:
        expenses_percentage = 15
    winnings = dancers * points + (dancers * points * 0.5)

total_expenses = winnings * (expenses_percentage / 100)
charity_amount = (winnings - total_expenses) * 0.75
remaining_amount = winnings - total_expenses - charity_amount
money_per_dancer = remaining_amount / dancers

print(f"Charity - {charity_amount:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")
