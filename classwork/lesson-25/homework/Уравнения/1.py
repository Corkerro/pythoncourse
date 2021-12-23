import math
pi = math.pi
x = float(input('Введите х ====>   '))
if x >(-pi) and x < pi/4:
    print(f'y = {(-math.cos(x-pi))**2}')
elif x>pi/4 and x<= 1:
    print(f'y = {math.sqrt(abs(x+1))}')
elif x>1:
    print(f'y = {1/(x-1)}')
else: print('Error')
