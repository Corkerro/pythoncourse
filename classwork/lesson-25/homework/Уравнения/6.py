import math
pi = math.pi
e = math.e
x = float(input('Введите х ====>   '))
if abs(x)<2:
    print(f'y = {x-e**x}')
elif x<=-2:
    print(f'y = {math.log10(x**2)}')
elif x>=2:
    print(f'y = {math.sin(x)**2}')