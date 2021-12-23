print('Задача №5')
print('\tВозьмем список недавно зарегистрированных, но еще не проверенных пользователей сайта.\n\tКак переместить пользователей после проверки в отдельный список проверенных пользователей?\n\tОдно из возможных решений: используем цикл while для извлечения пользователей из \n\tсписка непроверенных, проверяем их и включаем в отдельный список проверенных пользователей.')
ne_prov_spis = ['Roma','Igor','Max','Kolya']
prov_spis =[]
while ne_prov_spis:
    prov_spis.append(ne_prov_spis[0])
    ne_prov_spis.pop(0)
print(prov_spis)
code = input("Если хотите увидеть код напишите 'code' ====>   ")
if code =='code':
    print(f"\nne_prov_spis = ['Roma','Igor','Max','Kolya']\nprov_spis =[]\nwhile ne_prov_spis:\n\tprov_spis.append(ne_prov_spis[0])\n\tne_prov_spis.pop(0)\nprint(prov_spis)\n\n")