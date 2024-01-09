n = int(input())
numbers = []

for _ in range(n):
    num = int(input())
    numbers.append(num)

found = False
for i in range(n):
    current_num = numbers[i]
    sum_others = sum(numbers[:i] + numbers[i+1:])
    if current_num == sum_others:
        found = True
        print("Yes")
        print("Sum =", current_num)
        break

if not found:
    max_num = max(numbers)
    diff = abs(max_num - sum(numbers) + max_num)
    print("No")
    print("Diff =", diff)

