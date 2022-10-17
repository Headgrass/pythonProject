# Напишите программу, которая определит позицию второго вхождения строки
# в списке либо сообщит, что её нет.
#
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

lst = ['qwe', 'qwer', 'asd', 'dsa', 'qwe', 'dfsj']

n = (input("Введите строку поиска: "))

count = 0
for i in range(len(lst)):
    if (lst[i] == n) and count == 0:
        count = 1
        position_1 = i
    elif (lst[i] == n) and count == 1:
        position_2 = i
        count = 2

if count == 2:
    var = f'{n} входит в список {lst} на позициях {position_1} и {position_2}'
    print(var)
else: print('-1')
