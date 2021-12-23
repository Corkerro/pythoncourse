print('Задача №10')
print("\tДопустим, у нас есть словарь, который в качестве ключей содержит в себе определенные\n\tимена городов, имеющие некоторые числовые значения (длина города), и мы хотим удалить несколько городов\n\t(скажем, Дели и Лондон) вместе с их значениями. Переменная i отвечает за ключи словаря,\n\tа выражение d[i] вычисляет значение по этому ключу. Например, d['Mumbai'] возвратит 221.")
d = {'Mumbai': 223, 'Kharkiv': 214, 'Deli': 674, 'London': 258}
print(d)
del_spis = []
while True:
    del_kak = input('Какой из этих городов вы хотите удалить?(exit) ====>   ')
    if del_kak == 'exit':break
    else:
        del_spis.append(del_kak)    
        del d[del_kak]
print(f'Новый список - {d}\nСписок удаленных городов - {del_spis}')
code = input("Если хотите увидеть код напишите 'code' ====>   ")
if code =='code':
    print("\nd = {'Mumbai': 223, 'Kharkiv': 214, 'Deli': 674, 'London': 258}\nprint(d)\ndel_spis = []\nwhile True:\n\tdel_kak = input('Какой из этих городов вы хотите удалить?(exit) ====>   ')\n\tif del_kak == 'exit':break\n\telse:\n\t\tdel_spis.append(del_kak)\n\t\tdel d[del_kak]\nprint(f'Новый список - {d}\nСписок удаленных городов - {del_spis}')\n\n")