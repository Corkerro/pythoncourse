class User():
    def __init__(self,first_name,last_name,year_of_birdth,favortite_hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birdth = year_of_birdth
        self.favortite_hobby = favortite_hobby
    def describe_user(self):
        print(f'Name: {str(self.first_name).title()}\nLast name: {str(self.last_name).title()}\nYear of birdth : {self.year_of_birdth}\nFavorite hobby: {self.favortite_hobby}')
    def greet_user(self):
        print(f'Hello, {str(self.first_name).title()}! How are you?\n')
user1 = User('dima','Prohod`ko',2009,'Painting')
user1.describe_user()
user1.greet_user()
user2 = User('vlad','Goloborod`ko',2010,'collecting')
user2.describe_user()
user2.greet_user()
user3 = User('bogdan','Andrienko',1997,'Coding')
user3.describe_user()
user3.greet_user()
