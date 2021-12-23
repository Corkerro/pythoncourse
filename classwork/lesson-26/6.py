import math
p = math.pi

class Circle:
    def __init__(self,r):
        self.r = r
    def dlina_cicle(self):
        print(f'Длина: {2*p*self.r}')
    def square(self):
        print(f'Площадь: {p*(self.r**2)}')
kryg = Circle(5)
kryg.dlina_cicle()
kryg.square()
kryg2 = Circle(15)
kryg2.dlina_cicle()
kryg2.square()
kryg3 = Circle(13.14)
kryg3.dlina_cicle()
kryg3.square()