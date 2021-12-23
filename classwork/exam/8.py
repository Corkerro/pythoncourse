print('Задача №8')
print("\tДан словарь {'a': 2, 'b': 4, 'c': 6, 'd': 8} и отберем все значения больше 2")
dict = {'a': 2, 'b': 4, 'c': 6, 'd': 8}
for i in dict.values(): 
    if i > 2:print(i,end=';')
code = input("\nЕсли хотите увидеть код напишите 'code' ====>   ")
if code =='code':
    print("\ndict = {'a': 2, 'b': 4, 'c': 6, 'd': 8}\nfor i in dict.values(): \n\tif i > 2:print(i,end=';')\n\n")