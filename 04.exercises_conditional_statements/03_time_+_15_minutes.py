# Да се напише програма, която чете час и минути от 24-часово денонощие,
# въведени от потребителя и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат часове:минути. Часовете винаги са между 0 и 23,
# а минутите винаги са между 0 и 59. Часовете се изписват с една или две цифри.
# Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.


hour = int(input())
minute = int(input())

minute += 15
if minute >= 60:
    hour += 1
    minute -= 60

if hour >= 24:
    hour -= 24

print(f"{hour:02d}:{minute:02d}")
