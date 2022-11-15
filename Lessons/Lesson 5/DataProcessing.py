'''
Lambda - для создания анонимных маленьких функций
Map - применяет функцию к списку или словарю, возвращает измененный объект
Filter - применяет логическую функцию к списку или словарю, возвращает элементы,
которые удовлетворяют условию
Zip - создает кортежи из элементов словарей или списков
List comprehension - удобная генерация списков
'''

add = lambda x, y: x + y # тут что-то поменяли
# print(add(2, 3)) # результат: 5

def multiply2(x):
    return x * 2


# print(list(map(multiply2, [1, 2, 3, 4]))) # вернет [2, 4, 6, 8]

def check(x):
    if x > 10: return True
    else: return False

dict_a = [1, 11, 3, 6, 22, 88, 99, 0, 3]

res = list(filter(check, dict_a)) # Вернет: [{'11', '22', '88', '99'}]

# print(res)

a = [10, 20, 30, 40]
b = ['a', 'b', 'c', 'd', 'e']

# for i in zip(a, b): # zip - возвращает кортеж из попарных элементов переданных списков
#     print(i)

# spisok = [16, 46, 26, 36]
# for i in enumerate(spisok): # возвращает список, нумеруя индекс элементов
#     print(i)

# spisok2 = [16, 46, 26, 36]
# for i, value in enumerate(spisok2): # возвращает список, нумеруя индекс элементов
#     print(i, value)

squares = [x ** 2 for x in range(10)] # возвращает список от 0 до 9(вкл), возведенный в квадрат

odds = [x for x in range(10) if x % 2 != 0]  # возвращает список от 0 до 9(вкл), нечетных чисел


print(squares)

print(odds)

# Таблица умножения

# i = 1
# j = 1
# while i < 10:
#     while j < 10:
#         print(i * j, end="\t")
#         j += 1
#     print("\n")
#     j = 1
#     i += 1
