starting_number = int(input())

bonus_points = 0

if starting_number <= 100:
    bonus_points = 5
elif starting_number <= 1000:
    bonus_points = starting_number * 0.2
elif starting_number > 1000:
    bonus_points = starting_number * 0.1

bonus_extra_points = 0

if starting_number % 2 == 0:
    bonus_extra_points = 1

if starting_number % 10 == 5:
    bonus_extra_points = bonus_extra_points + 2

print(bonus_points + bonus_extra_points)
print(starting_number + bonus_points + bonus_extra_points)
