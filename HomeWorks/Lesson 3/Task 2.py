# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# *Пример:*
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import math

lst = [2, 3, 4, 5, 6]

size = math.ceil(len(lst)/2)
res = []
for i in range(size):
    res.append(lst[i]*lst[-i - 1])
print(res)
