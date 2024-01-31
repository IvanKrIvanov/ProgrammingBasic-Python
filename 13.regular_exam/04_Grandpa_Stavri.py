N = int(input())
total_liters = 0
total_degrees = 0

for _ in range(N):
    liters = float(input())
    degrees = float(input())
    total_liters += liters
    total_degrees += (liters * degrees)

average_degrees = total_degrees / total_liters

print(f"Liter: {total_liters:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38:
    print("Not good, you should baking!")
elif average_degrees >= 38 and average_degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")
