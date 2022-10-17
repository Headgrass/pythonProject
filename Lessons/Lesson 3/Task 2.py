# Задайте список из 2*N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

try:
    sp = []
    n = int(input("Введите число: "))

    for i in range(-n, n + 1):
        sp.append(i)
    with open('file.txt', 'r') as data:
        a = data.readline()
        b = data.readline()

    print(a, b)
    a = int(a)
    b = int(b)

    print(sp)
    print(f'Произведение элементов равно {sp[a] * sp[b]}')

except:
    print("надо было вводить именно целое число")

