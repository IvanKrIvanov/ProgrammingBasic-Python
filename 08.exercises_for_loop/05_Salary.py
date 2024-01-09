FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50

opened_tab = int(input())
salary = float(input())

for _ in range(opened_tab):
    current_opened_tab = input()

    if current_opened_tab == "Facebook":
        salary -= FACEBOOK_FINE
        if salary <= 0:
            print("You have lost your salary.")
            break

    if current_opened_tab == "Instagram":
        salary -= INSTAGRAM_FINE
        if salary <= 0:
            print("You have lost your salary.")
            break

    if current_opened_tab == "Reddit":
        salary -= REDDIT_FINE
        if salary <= 0:
            print("You have lost your salary.")
            break

if salary > 0:
    print(f"{int(salary)}")
