import math
pi = math.pi
e = math.e
x = float(input('Введите х ====>   '))
if x>1 and x <3.2:
    print(f'y = {-((1.4+x)/math.log(x))}')
elif x>0 and x<=1:
    print(f'y = {x**2 - 0.75}')
elif x<=0:
    print(f'y = {math.cos(x**2)**3-math.sin(x**2)**3}')
else: print('ERROR')