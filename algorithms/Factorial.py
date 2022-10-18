n = int(input("Введите число для поиска факториала: "))
sum = 1
var = 1

for i in range(var, n):
    if var <= n:
        sum = sum * (var + 1)
        var = var + 1
print(f'Сумма факториала {n} равна {sum}')