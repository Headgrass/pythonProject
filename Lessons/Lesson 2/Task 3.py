#  Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
import math

try:
    N = int(input("Enter sum iter: "))
    for i in range(N):
        print(math.pow(-3, i))
except:
    print("Invalid incorrect data")
