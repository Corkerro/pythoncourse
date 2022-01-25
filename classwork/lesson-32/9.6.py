class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f'Restaurant \'{self.restaurant_name}\'. Cuisine type : {self.cuisine_type}\n\n')
    def restaurant_open(self):
        print(f'Restaurant \'{self.restaurant_name}\' is open\n\n')
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type,flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    def flavors_list(self):
        print(f'Flavors list: {self.flavors}')
iceCreamStand=IceCreamStand('Morozenko', 'Ice', 'Type 1,Type 2,Type 3,Type 4,Type 5,Type 6,Type 7')
iceCreamStand.describe_restaurant()
iceCreamStand.flavors_list()