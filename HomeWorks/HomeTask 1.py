# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

print("Программа принимает на вход день недели и проверяет, является ли этот день выходным")
day = int(input("Введите число "))
if day == 6 or day == 7:
    print("ВЫХОДНОЙ")
else:
    print("День недели не является выходным")