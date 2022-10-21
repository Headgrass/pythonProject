# lst = [1, 2, 3, 5, 8, 15, 23, 38]
# # lst2 = [lst. append(i) for i in range(len(lst)) if i % 2 == 0]
#
# def f(x):
#     return x**2
#
# res = [(i, f(i)) for i in range(len(lst)) if i % 2 == 0]
# print(res)

# path = 'file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()
#
# numbers = []
#
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]
#
# out = []
#
# for e in numbers:
#     if not e % 2:
#         out.append((e, e **2))
# print(out)

# li = [x for x in range(1, 21)]
# data = list(map(int, input("Введите числа: ").split()))
# li = list(map(lambda x: x+10, data))
# print(li)

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
#
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# data = [x for x in range(10)]
#
# res = list(filter(lambda x: not x % 2, data))
# print(res)

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
#
# data = list(zip(users, ids, salary))
# # data = list(enumerate(users))
# print(data)


# items = list(range(2021))
# print(items[:2022])  # [0, 1, 2, 3, 4]


