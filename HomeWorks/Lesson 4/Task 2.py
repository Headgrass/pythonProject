# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

lst = [1, 2, 1, 3, 4, 3, 5, 4, 6, 5]  # ожидаем увидеть [1, 2, 3, 4, 5, 6]
print(f'Изначальный список: {lst}')
res = []

[res.append(i) for i in lst if i not in res]
print(f'Список неповторяющихся элементов: {res}')
