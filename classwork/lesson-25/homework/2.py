class Animals:
    def __init__(self,name,type,class_,rod,vid):
        self.name = name
        self.type = type
        self.class_ = class_
        self.rod = rod
        self.vid = vid
        print(f"Название: {self.name}\nТип: {self.type}\nКласс {self.class_}\nРод: {self.rod}\nВид: {self.vid}\n")
animal_taipan = Animals('Тайпан','Хордовые','Пресмыкающиеся','Тайпаны','Змея')
animal_zayac = Animals('Антилоповый заяц','Хордовые','Млекопитающие','Зайцы','Антилоповый заяц')
animal_lev = Animals('Лев','Хордовые','Млекопитающие','Пантеры','Лев')
animal_geaprd = Animals('Гепард','Хордовые','Млекопитающие','Гепарды','Гепард')
animal_lenivec = Animals('Трёхпалые ленивцы','Хордовые','Млекопитающие','Род трёхпалых ленивцев','Трёхпалые ленивцы')