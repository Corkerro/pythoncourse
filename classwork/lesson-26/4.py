import math
pi = math.pi
e = math.e
x = float(input('Введите х ====>   '))
if x>=1:
    print(f'y = {e**(-abs(x))}')
elif abs(x)<1:
    print(f'y = {math.log10(math.sqrt(1-x**2))}')
elif x<= -1:
    print(f'y = {math.sin(x)**2}')
else: print('ERROR')