current_height = 5364
days = 0

while True:
    rest = input()
    if rest == "END" or current_height >= 8848 or days > 5:
        break

    overnight = rest == "Yes"
    meters_climbed = int(input())
    days += 1

    if overnight:
        current_height += meters_climbed
    else:
        current_height += meters_climbed

    if current_height >= 8848:
        print(f"Goal reached for {days} days!")
        break

if current_height < 8848:
    print("Failed!")
    print(current_height)
