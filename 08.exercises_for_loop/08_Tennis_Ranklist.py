import math

W_POINTS = 2000
F_POINTS = 1200
SF_POINTS = 720

tournament_count = int(input())
starting_points = int(input())

gained_points = 0
total_win = 0

for _ in range(tournament_count):
    tournament_result = input()
    if tournament_result == "W":
        gained_points += W_POINTS
        total_win += 1
    elif tournament_result == "F":
        gained_points += F_POINTS
    elif tournament_result == "SF":
        gained_points += SF_POINTS
total_points = starting_points + gained_points
average_points = math.floor(gained_points / tournament_count)
w_percents = total_win / tournament_count * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{w_percents:.2f}%")
