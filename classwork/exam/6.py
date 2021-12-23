print('Задача №6')
print("\tПредставьте, что вы создали список своих любимых блюд ['pizza', 'falafel', 'carrot cake']\n\tи теперь хотите создать отдельный список блюд, которые нравятся вашему другу.\n\tПока вашему другу нравятся все блюда из нашего списка, поэтому вы можете создать другой список\n\tпростым копированием своего.Добавить в список друга любимое мороженое, которого нет в вашем\n\tсписке. Мороженое ввести с клавиатуры. Вывести на экран блюда, которые нравятся вам и отдельно\n\tвывести которые нравятся вашему другу – перебором каждого элемента в списке. ")
my_spisok = ['pizza', 'falafel', 'carrot cake'] 
friend_spisok = my_spisok[:]
icecream = input('Введите название мороженого ====>   ')
friend_spisok.append(icecream)
print('\t\tМои люимые блюда:')
for i in my_spisok:
    print(i,end='\t')
print('\n\t\tЛюбимые блюда друга:')
for i in friend_spisok:
    print(i,end='\t')
code = input("\nЕсли хотите увидеть код напишите 'code' ====>   ")
if code =='code':
    print(f"\n\nmy_spisok = ['pizza', 'falafel', 'carrot cake'] \nfriend_spisok = my_spisok[:]\nicecream = input('Введите название мороженого ====>   ')\nfriend_spisok.append(icecream)\nprint('\t\tМои люимые блюда:')\nfor i in my_spisok:\n\tprint(i,end=';\t')\nprint('\n\t\tЛюбимые блюда друга:')\nfor i in friend_spisok:\n\tprint(i,end='\t')\n\n")