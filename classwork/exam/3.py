print('Задача №3')
print('\tНапишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.')
print('\tnumbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953,\n\t345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]')
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]
for i in numbers:
    if i !=237:
        if i%2 == 0:
            print(i, end= ';')
    else:break
code = input("Если хотите увидеть код напишите 'code' ====>   ")
if code =='code':
    print(f"\nnumbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]\nfor i in numbers:\n\tif i !=237:\n\t\tif i%2 == 0:\n\t\t\tprint(i, end= ';')\n\telse:break\n\n")