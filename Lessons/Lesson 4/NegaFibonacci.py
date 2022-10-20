# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Мегафибоначчи]
'''
try:
    n = int(input("Введите число: "))

    fib1 = [0, 1]
    fib2 = [0, 1]

    for i in range(1, n):
        summa = fib1[i] + fib1[i-1]
        fib1.append(summa)

    fib1.remove(0)

    for i in range(1, n):
        summa = fib2[i-1] - fib2[i]
        fib2.append(summa)

    fib2 = list(reversed(fib2))

    print(fib2 + fib1)

except:
    print("Введены некорректные данные!")


number = int(input("Введите целое число: "))
list_pos = [0, 1]
list_neg = [0, 1]
for i in range(number-1):
    list_pos.append(list_pos[-1] + list_pos[-2])
    list_neg.append(list_neg[-2] - list_neg[-1])

list_result = list_neg[::-1] + list_pos[1:]

print(list_result)

'''

num = int(input("Введите целое число: "))
result = [1, 0, 1]
while num !=1:
    k = (result[-1]+result[-2])
    result.append(k)
    result.insert(0, (-1)**(num+1)*k)
    num -= 1
print(result)