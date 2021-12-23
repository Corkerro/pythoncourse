import math
pi = math.pi
e = math.e
x = float(input('Введите х ====>   '))
if x>=0 and x<2:
    print(f'y = {x*math.sqrt(abs(x - 5.4))}')
elif x>=2 and x<8:
    print(f'y = {math.atan(x)**2}')
elif x>= 8:
    print(f'y = {math.log(abs(x-7.8))}')
else: print('ERROR')
