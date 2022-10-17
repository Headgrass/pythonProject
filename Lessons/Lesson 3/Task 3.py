# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

lst = ["235", "basket", "3532", "cup", "5", "8", "10", "lines"]
print(lst)
n = input("Введите число: ")

# Вариант выводит True или False
# print(n in lst)

# Вариант выводит текст
for i in lst:
    count = 0
    if n in i:
        count = 1
        print("Да, есть")
        break
if count == 0:
        print("Не, нету")

