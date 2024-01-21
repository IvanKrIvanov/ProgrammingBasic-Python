start = int(input())
final = int(input())
magic_number = int(input())

combination_found = False
combinations_count = 0

for num1 in range(start, final + 1):
    for num2 in range(start, final + 1):
        combinations_count += 1
        if num1 + num2 == magic_number:
            combination_found = True
            break

    if combination_found:
        break

if combination_found:
    print(f"Combination N:{combinations_count} ({num1} + {num2} = {magic_number})")
else:
    print(f"{combinations_count} combinations - neither equals {magic_number}")
