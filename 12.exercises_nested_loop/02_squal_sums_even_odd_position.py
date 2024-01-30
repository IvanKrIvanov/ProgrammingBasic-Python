# start_number = int(input())
# end_number = int(input())
#
# found_numbers = []
#
# for num in range(start_number + 1, end_number):
#     digits = [int(digit) for digit in str(num)]
#     even_sum = sum(digits[1::2])
#     odd_sum = sum(digits[0::2])
#
#     if even_sum == odd_sum:
#         found_numbers.append(str(num))
#
# result = ' '.join(found_numbers)
# print(result)
start_number = int(input())
end_number = int(input())

output = ""

for num in range(start_number + 1, end_number):
    digits = [int(digit) for digit in str(num)]
    even_sum = sum(digits[1::2])
    odd_sum = sum(digits[0::2])

    if even_sum == odd_sum:
        output += str(num) + " "

print(output.strip())

