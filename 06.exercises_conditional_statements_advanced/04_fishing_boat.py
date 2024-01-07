budget = int(input())
season = input()
fisherman = int(input())

boat_coast = 0
discount = 0
extra_discount = 0
if season == "Spring":
    boat_coast == 3000
if season == "Summer" or season == "Autumn":
    boat_coast == 4200
elif season == "Winter":
    boat_coast == 2600

if fisherman <= 6:
    discount = 0.10
elif fisherman <= 11:
    discount = 0.15
else:
    discount = 0.25

if fisherman % 2 == 0 and season != "Autumn":
    extra_discount = 0.05

total_coast = boat_coast * (1 - discount) * (1- extra_discount)
if budget >= total_coast:
    print(f"Yes! You have {budget - total_coast:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_coast - budget:.2f} leva.")

