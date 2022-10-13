# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

book = {}
n = int(input("Enter sum elem: "))

for i in range(n):
    book[i+1] = (i+1)*3+1
print(book)