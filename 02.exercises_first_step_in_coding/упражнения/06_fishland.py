scum_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_price = scum_price * 1.6
safrid_price = caca_price * 1.8
price_midi = 7.5

total_price = scum_price + caca_price + palamud_price + safrid_price + (price_midi * midi_kg)
print(f'{total_price:.2}')

