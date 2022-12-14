# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# *Пример:*
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial

try:
    n = int(input('Введите число: '))
    fact = lambda x: ((x == 1) and 1) or x * factorial(x - 1)
    list2 = list(fact(i) for i in range(1, n + 1))
    print(list2)
except:
    print("Invalid incorrect data")
