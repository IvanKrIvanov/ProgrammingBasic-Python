n = int(input())
sum_even = 0
sum_odd = 0

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

if sum_even == sum_odd:
    print("Yes")
    print("Sum =", sum_even)
else:
    diff = abs(sum_even - sum_odd)
    print("No")
    print("Diff =", diff)
