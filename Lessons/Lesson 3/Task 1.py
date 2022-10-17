# Задайте список из n чисел последовательности (1+1/N)**N и выведите на экран их сумму.

def sum_numbers(a):
    return (1+1/a)**a

try:
    n = int(input("Введите число: "))
    sp = []
    for i in range(n):
        sp.append(sum_numbers(i + 1))
    print(sum(sp))
except:
    print("надо было вводить именно целое число")