class Restaurant():
    def __init__(self,restaurant_name,cuisine_type, number_served):
        number_served=0
        self.number_served = number_served
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f'Restaurant \'{self.restaurant_name}\'. Cuisine type : {self.cuisine_type}')
    def restaurant_open(self):
        print(f'Restaurant \'{self.restaurant_name}\' is open')
    def set_numer_served(self,n):
        self.number_served+=n
        print(f'Number served: {self.number_served}')
    def increment_number_served(self,m):
        self.number_served+=m
        print(f'New number served: {self.number_served}')
restauran = Restaurant('Y Ashota', 'Armyanskaya',0)
restauran.describe_restaurant()
restauran.restaurant_open()
m= int(input('Введите m ====>   '))
restauran.set_numer_served(20)
restauran.increment_number_served(m)