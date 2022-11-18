# def BinarySearch(massive, find):
#     left = 0
#     right = len(massive - 1)

n = int(input("Введите число: "))
i = 1
j = 1
while i < n:
    while j < n:
        print(i * j)
        j += 1
    i += 1
