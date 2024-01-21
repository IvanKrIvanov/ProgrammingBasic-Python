number_of_flours = int(input())
number_of_rooms = int(input())
floor_letter = ""
for current_flour in range(number_of_flours, 0, -1):
    if current_flour == number_of_flours:
        floor_letter = "L"
    elif current_flour % 2 == 0:
        floor_letter = "O"
    else:
        floor_letter = "A"
    for current_room in range(number_of_rooms):
        print(f"{floor_letter}{current_flour}{current_room}", end = " ")
    print()

