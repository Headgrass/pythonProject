# Найдите корни квадратного уравнения Ax² + Bx + C = 0 ) с помощью математических формул
# нахождения корней квадратного уравнения

import math
a = int(input("Введите коэффицент А: "))
b = int(input("Введите коэффицент В: "))
c = int(input("Введите коэффицент С: "))

d = b**2 - 4 * a * c

if d > 0:
    x1 = (-b + (math.isqrt(d)) / (2 * a))
    x2 = (-b - (math.isqrt(d)) / (2 * a))
    print(f"Найдено два корня {x1} и {x2}")
elif d == 0:
    x1 = -b/(2 * a)
    print(f"Уравнение имеет один корень {x1} ")
else:
    print("Корней нет")