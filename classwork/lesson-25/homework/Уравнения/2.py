import math
pi = math.pi
e = math.e
x = float(input('Введите х ====>   '))
y = float(input('Введите y ====>   '))
if abs(x*y)<1 and x < 0:
    print(f'Z = {(x+y)/e**(x*y)}')
elif x>2 and y<=0:
    print(f'Z = {-math.log(x)**2}')
elif y>0 and x>=0 and x<=2:
    print(f'Z = {math.log10(math.sqrt(y))}')
else: print('ERROR')

