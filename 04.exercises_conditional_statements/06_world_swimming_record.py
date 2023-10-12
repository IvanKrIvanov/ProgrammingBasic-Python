# Иван трябва да преплува 1500 м.:  1500 * 20 = 30000 сек.
# На всеки 15 м. към времето му се добавят 12.5 сек.:
# 1500 / 15 = 100 * 12.5 = 1250 сек.
# Общо време: 30000 + 1250 = 31250 сек.
# 10464 < 31250
# Времето, което не му е стигнало за да подобри рекорда:
# 31250 – 10464 = 20786 сек.

import math


record = float(input())
distance = float(input())
time_per_meter = float(input())

water_resistance = math.floor(distance / 15) * 12.5
ivan_time = distance * time_per_meter + water_resistance

if ivan_time < record:
    print(f'Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.')
else:
    missing_seconds = ivan_time - record
    print(f'No, he failed! He was {missing_seconds:.2f} seconds slower.')


