from math import pi

type_of_the_figure = input()
area = 0

if type_of_the_figure == 'square':
    side = float(input())
    area = side * side


elif type_of_the_figure == 'rectangle':
    first_side = float(input())
    second_side = float(input())
    area = first_side * second_side

elif type_of_the_figure == 'circle':
    radius = float(input())
    area = pi * (radius ** 2)


elif type_of_the_figure == 'triangle':
    length = float(input())
    height = float(input())
    area = length * height / 2

print(f'{area:.3f}')
