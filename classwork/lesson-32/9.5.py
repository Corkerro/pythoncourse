class User():
    def __init__(self,first_name,last_name,year_of_birdth,favortite_hobby,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birdth = year_of_birdth
        self.favortite_hobby = favortite_hobby
        self.login_attempts = login_attempts
    def describe_user(self):
        print(f'Name: {str(self.first_name).title()}\nLast name: {str(self.last_name).title()}\nYear of birdth : {self.year_of_birdth}\nFavorite hobby: {self.favortite_hobby}')
    def greet_user(self):
        print(f'Hello, {str(self.first_name).title()}! How are you?\n')
    def incriment_login_attempts(self):
        self.login_attempts+=1
        print(f'Login attempts: {self.login_attempts}')
    def reset_login_attempts(self):
        self.login_attempts=0
        print(f'Login attempts: {self.login_attempts}')
user1 = User('dima','Prohod`ko',2009,'Painting',0)
user1.describe_user()
user1.greet_user()
user1.incriment_login_attempts()
user1.incriment_login_attempts()
user1.incriment_login_attempts()
user1.reset_login_attempts()


