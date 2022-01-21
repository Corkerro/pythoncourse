
class Car():
    def __init__(self,marka,model,year,adomiter):
        adomiter = 0
        self.marka = marka
        self.model = model
        self.year = year
        self.adomiter = adomiter
    def get_discript_name(self):
        print(f'\n\nМарка машини: {self.marka}\nМодель: {self.model}\nГод: {self.year}')
    def read_adomiter(self):
        print(f'Адометр:{self.adomiter}')    
    def appdate(self,adomiter_value):
        print(f'Новый адометр: {adomiter_value}')
    def probeg_adomint(self,myprobeg):
        print(f'После использование пробег становит: {probeg+myprobeg}')
    
my_new_car= Car('BMW','M3',2016,0)
my_new_car.adomiter = 23
while True:
    probeg= int(input('Введите probeg ====>   '))
    if probeg < my_new_car.adomiter:
        print(f'Скручивать нельзя!')
    else: break

my_new_car.get_discript_name()
my_new_car.read_adomiter()
my_new_car.appdate(probeg)
my_new_car.probeg_adomint(probeg)
