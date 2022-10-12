# Task 3
print("Программа принимает на вход число N и выводить числа от -N до N")

n1 = int(input("Введите число: "))
print(list(range(-n1, n1 + 1)))

'''
n2 = n1 * -1

while n2 in range(n2-1, n1+1):
    print(n2)
    n2 = n2+1
'''