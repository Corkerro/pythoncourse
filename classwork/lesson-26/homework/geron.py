import math
a = int(input("Введите a ====>   "))
b = int(input("Введите b ====>   "))
c = int(input("Введите c ====>   "))
if a+b > c and a+c>b and c+b>a:
    p = (a+b+c)/2
    print(f"Площадь треугольника {math.sqrt(p*(p-a)*(p-b)*(p-c))} см")
else: print('К сожалению такого треугольника не существует.')