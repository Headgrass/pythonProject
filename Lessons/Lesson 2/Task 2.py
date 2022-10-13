# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве

from math import sqrt

x1 = float(input("Enter X coordinate 1: "))
y1 = float(input("Enter Y coordinate 1: "))


x2 = float(input("Enter X coordinate 2: "))
y2 = float(input("Enter Y coordinate 2: "))

result = sqrt((x2 - x1)**2 + (y2 - y1) **2)
print(round(result, 2))
