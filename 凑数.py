import random

fang = [489008, 485100, 475786, 671168, 466685, 452293, 513329,
        460882, 462715, 474728, 472591, 452639, 477647, 472953]
chewei = [68000, 68000, 61791, 74800, 74362, 78200, 77350, 78200, 74363]

a = 0
b = 0
c = 0
sum = 0

while True:
    a = int(random.choice(fang))
    list_b = random.sample(chewei, 2)
    b = int(list_b[0])
    c = int(list_b[1])
    sum = a + b + c
    if sum == 662054:
        print(a, b, c, sep='，')
        break