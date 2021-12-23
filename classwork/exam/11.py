print('Задача №11')
print("\tПроверяем четность числа и ставим данному ключу в соответствие значение\n\tлибо ‘odd’ (нечетное), либо ‘even’ (четное). dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}")
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for i in dic:
    if dic[i]%2 == 0:
        print(f'{dic[i]} - even')
    else:print(f'{dic[i]} - odd')
code = input("Если хотите увидеть код напишите 'code' ====>   ")
if code =='code':
    print("\ndic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}\nfor i in dic:\n\tif dic[i]%2 == 0:\n\t\tprint(f'{dic[i]} - even')\n\telse:print(f'{dic[i]} - odd')\n\n")