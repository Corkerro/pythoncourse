class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f'Restaurant \'{self.restaurant_name}\'. Cuisine type : {self.cuisine_type}\n\n')
    def restaurant_open(self):
        print(f'Restaurant \'{self.restaurant_name}\' is open\n\n')
restauran1 = Restaurant('Y Ashota', 'Armyanskaya')
restauran1.describe_restaurant()
restauran1.restaurant_open()