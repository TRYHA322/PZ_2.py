# Задание №1
spis = (123,'Строка', 3.0 , True )
for i in spis:
    print(i , type(i))
# Задание №2
spis = list()
i = ''
while i != 'end':
    i = input('Введите значение, для завершения введите "end": ')
    if i != 'end':
        spis.append(i)
for i in range(0 , len(spis)-1, 2):
    spis[i] , spis[i+1] = spis[i+1] , spis[i]
print(spis)
# Задание №3
season = {
(1 , 2 , 12) :'Зима' ,
(3 , 4 , 5) :'Весна' ,
(6 , 7 , 8) :'Лето' ,
(9 , 10 , 11) : 'Осень'
}
mouth = int(input('Введите номер месяца: '))
for i in season.keys():
    for j in i:
        if j == mouth:
            print(season.get(i))
            break
# Задание №4
spis = list(input('Введите строку: ').split(' '))
num = 0
for i in spis:
    num += 1
    if len(i) <= 10:
        print(f'{num}. {i}')
    else:
        print(f'{num}. {i[0:10]}')
# Задание №5
my_list = [7, 5, 3, 3, 2]
k = ''
while k != 'end':
    k = input('Введите число, для окончания напишите "end": ')
    if k != 'end':
        for i in range(len(my_list) - 1):
            print(my_list[i])
            if my_list[-1] > int(k):
                my_list.append(int(k))
                break
            elif my_list[i] <= int(k):
                my_list.insert(i , int(k))
                break
print(my_list)
# Задание №6
list_name = []
list_price = []
list_am = []
list_unit = []
name = None
i = 0
my_list = []
while name != 'end':
    i += 1
    name = input('Введите название товара, для завершения введите "end" : ')
    if name != 'end':
        price = int(input('Введите цену товара: '))
        am = int(input('Введите количество товара: '))
        unit = input('Введите ед. товара: ')
        my_dict = {
          'название' : name ,
            'цена' : price ,
            'количество' : am ,
            'ед.' : unit
        }
        my_tuple = ( i , my_dict )
        my_list.append(my_tuple)
print(my_list)
for i in my_list:
    j = i[1]
    list_name.append(j.get('название'))
    list_price.append(j.get('цена'))
    list_am.append(j.get('количество'))
    list_unit.append(j.get('ед.'))
my_dict = {
          'название' : list_name ,
            'цена' : list_price ,
            'количество' : list_am ,
            'ед.' : list_unit
        }
print(my_dict)





