# Алгоритм Евклида

def euclideanAlgorithm(x, y):
    count = 0
    while x != 0:
        count = count + 1
        if x > y:
            x = x - y
        else:
            y = y - x
        break
    print(f'EuclideanAlgorithm, count: {count}')
    return x


euclideanAlgorithm(100, 2054)

arr = [6, 2, -3, 15, 9]
for i in range(len(arr)):
    min = i
    for j in i + 1:
        if arr[j] < arr[min]:
            min = j

print(arr)


