print('Задача №4')
print('\tПериоды жизни: напишите цепочку if-elif-else для определения периода жизни человека.\n\tПрисвойте значение переменной age, а затем выведите сообщение: ')
print('\t• Если значение меньше 2 — младенец. \n\t• Если значение больше или равно 2, но меньше 4 — малыш.\n\t• Если значение больше или равно 4, но меньше 13 — ребенок.\n\t• Если значение больше или равно 13, но меньше 20 — подросток. \n\t• Если значение больше или равно 20, но меньше 65 — взрослый.\n\t• Если значение больше или равно 65 — пожилой человек.')
age = int(input('Введите возраст =====>     '))
if age < 2: print('Младенец')
elif age < 4:print('Малыш')
elif age < 13:print('Ребенок')
elif age < 20:print('Подросток')
elif age < 65:print('Взрослый')
else:print('Пожилой')
code = input("Если хотите увидеть код напишите 'code' ====>   ")
if code =='code':
    print(f"\nage = int(input('Введите возраст =====>     '))\nif age < 2: print('Младенец')\nelif age < 4:print('Малыш')\nelif age < 13:print('Ребенок')\nelif age < 20:print('Подросток')\nelif age < 65:print('Взрослый')\nelse:print('Пожилой')\n\n")