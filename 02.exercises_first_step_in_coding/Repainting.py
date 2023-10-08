NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
PAINT_THINNER_PRICE = 5.00
BAG_PRICE = 0.40

nylon_quantity = int(input())
paint_quantity = int(input())
paint_thinner_quantity = int(input())
works_hours = int(input())

paint_quantity_extra = 0.10 * paint_quantity
nylon_quantity_extra = 2

total_price_material = (nylon_quantity + nylon_quantity_extra) * NYLON_PRICE \
    + (paint_quantity + paint_quantity_extra) * PAINT_PRICE \
    + paint_thinner_quantity * PAINT_THINNER_PRICE \
    + BAG_PRICE

work_per_hours_price = total_price_material * 0.30
total_price = total_price_material + work_per_hours_price * works_hours

print(total_price)