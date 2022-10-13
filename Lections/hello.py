def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5)) # !!!!!
print(new_string('!'))    # !!!
print(new_string(4))      # 12


def concatenatio(*params):
    res = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', 'b', 'c', 'd', 'e')) # abcd
print(concatenatio('a', '1')) # a1


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)


# Кортеж (неизменяемый список)

a = (3, 5, 8, 4, 9)
print(a)
print(a[3])

# Преобразование

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))
# r: red g:green b:blue

dictionary = {}
dictionary = \
    {
        'up': 'upp',
        'left': 'leftt',
        'down': 'downn',
        'right': 'rightt'
    }
print(dictionary) # {'up': 'upp', 'left': 'leftt', 'down': 'downn', 'right': 'rightt'
print(dictionary['up'])
dictionary['up'] = 'up'
print(dictionary['left']) # leftt
# типы ключей могут отличаться

for k in dictionary.keys():
    print(k)

# МНОЖЕСТВА

colors = {'red', 'green', 'blue'}
print(colors)   # {'red', 'green', 'blue'}
colors.add('red')
print(colors)   # {'red', 'green', 'blue'}
colors.add('greay')
print(colors)   #{'red', 'green', 'blue', 'gray}
colors.remove('red')
print(colors)   #{'green', 'blue', 'gray}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors)   #{'green', 'blue', 'gray'}
colors.clear()  # {}
print(colors)   # set()


a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()
u = a.union(b)          # c = {1, 2, 3, 5, 8}
i = a.intersection(b)   # u = {1, 2, 3, 5, 8, 13, 21}
dl = a.difference(b)    # dl = {1, 3}
dr = b.difference(a)    # dr = {13, 21}

q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13}

s = frozenset(a)        # замороженное множество

