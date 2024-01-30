film_name = input()

total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while film_name != "Finish":
    seats = int(input())
    sold_tickets = 0

    ticket_type = input()
    while ticket_type != "End":
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

        sold_tickets += 1
        total_tickets += 1

        if sold_tickets >= seats:
            break

        ticket_type = input()

    percentage_full = (sold_tickets / seats) * 100
    print(f"{film_name} - {percentage_full:.2f}% full.")

    film_name = input()

percentage_student = (student_tickets / total_tickets) * 100
percentage_standard = (standard_tickets / total_tickets) * 100
percentage_kid = (kid_tickets / total_tickets) * 100

print(f"Total tickets: {total_tickets}")
print(f"{percentage_student:.2f}% student tickets.")
print(f"{percentage_standard:.2f}% standard tickets.")
print(f"{percentage_kid:.2f}% kids tickets.")
