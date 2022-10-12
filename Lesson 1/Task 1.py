# Task 1
print("Программа проверяет 2 числа на квадратность")
try:
    a = int(input('Введите а='))
    b = int(input('Введите b='))
    if (a ** 2 == b) or (b * b == a):
        print("да")
    else:
        print("Нет")
except:
    print("Введены некорректные данные!")
