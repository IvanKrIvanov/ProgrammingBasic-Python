width = float(input()) * 100
height = float(input()) * 100

corridor = 100

desk_width = 70
workspace_width = 120
desks_per_row = int(width // (desk_width + workspace_width))

desk_height = 70
workspace_height = 80
rows_per_side = int((height - workspace_height) // (desk_height + workspace_height))

seats_per_side = desks_per_row * rows_per_side

total_seats = seats_per_side * 2 - 3

print(total_seats)
