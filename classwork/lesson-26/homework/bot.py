class Bot:
    def __init__(self,name,age,country,favorite_subject,favorite_singer):
        self.name = name
        self.age = age
        self.country = country
        self.favorite_subject = favorite_subject
        self.favorite_singer = favorite_singer
    def all_info(self):
        print('И так, в ходе нашего разговора мне удалось собрать о тебе такую информацию:')
        print(f"Имя: {self.name}\nВозраст: {self.age}\nСтрана: {self.country}\nЛюбимый предмет: {self.favorite_subject}\nЛюбимий певец: {self.favorite_singer}\n")
_name = input('Привет, я 🤖Бот, давай познакомимся. Какое твоё имя?\n')
_age = input(f'Привет, {_name}, сколько тебе лет?\n')
_country = input('А в какой стране ты живешь?\n')
_favorite_subject = input('Какой твой любимый предмет в школе🧧?\n')
_favorite_singer = input('Какой твой любимый певец🤘?\n')
pers = Bot(_name,_age,_country,_favorite_subject,_favorite_singer)
pers.all_info()