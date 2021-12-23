print('Задача №2')
print('\tВыведите первый и последний элемент списка.\n\tЭлементы списка это рандомные числа от 0 до 15, количество элементов ввести с клавиатуры.\n\tПеремножить все элементы списка, вывести результат.')
import random
count = int(input('Введите число элементов в списке ====>   '))
spisok = []
c = 1
for i in range(count):
    spisok.append(random.randint(0,15))
print(spisok)
print(f'Первый элемент списка : {spisok[0]}. Последний элемент : {spisok[-1]}')
for i in spisok:
    c*=i
print(f'При умножении всех этих чисел получили : {c}')
code = input("Если хотите увидеть код напишите 'code' ====>   ")
if code =='code':
    print(f"\nimport random\ncount = int(input('Введите число элементов в списке ====>   '))\nspisok = []\nc = 1")
    print(f"for i in range(count):\n\tspisok.append(random.randint(0,15))\nprint(spisok)\nprint(f'Первый элемент списка : {spisok[0]}. Последний элемент : {spisok[-1]}')\nfor i in spisok:\n\tc*=i\nprint(f'При умножении всех этих чисел получили : {c}'')\n\n")