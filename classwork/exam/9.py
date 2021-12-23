print("Задача №9")
print("\tСоздать 2 списка с 6 элементами, один из которых будут целые числа.\n\tСоздать единый словарь, в котором будет храниться название с первого списка – key, второе  –  value\n\tзначение этого ключа, которое будет возводиться в степень степень будет вводится с клавиатуры.\n\tВывести предложение – «Я знаю твой ключ – «key», его значение является «value»")
import random
keys = ['key1','key2','key3','key4','key5','key6']
values =[]
for i in range(1,7):
    values.append(random.randint(1,18))
stepen = int(input('Введите степень ====>   '))
print(f'Keys - {keys}\nValues - {values}')
c = 0
for i in keys:
    print(f'Значение {i} - {values[c]**stepen}')
    c+=1
code = input("Если хотите увидеть код напишите 'code' ====>   ")
if code =='code':
    print("\nimport random\nkeys = ['key1','key2','key3','key4','key5','key6']\nvalues = []\nfor i in range(1,7):\n\fvalues.append(random.randint(1,18))\nstepen = int(input('Введите степень ====>   '))\nprint(f'Keys - {keys}\nValues - {values}')\nc = 0\nfor i in keys:\n\tprint(f'Значение {i} - {values[c]**stepen}')\n\tc+=1\n\n")