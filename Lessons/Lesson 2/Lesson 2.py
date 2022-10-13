
sp = []
sp.append(True)
sp = sp + [1221, "ыфва", 5696, [1, 3, 8, 9]]
print(sp)

sp.insert(0, 5555)
print("after insert ", sp)

print(sp[-1][-1])

a = sp.pop(-1)
print("after pop ", a)
print("")

# a.remove(2)
# print("after remove", a)
# for i in a: print(i)

mas_2dim = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(i+j)
    mas_2dim.append(temp)

for i in range(len(mas_2dim)):
    print(mas_2dim[i])


book = {}

book['Миша'] = 6569798654
book['Саша'] = [646549546,646156514521]

print(book)

if 'Миша' in book:
    print('Yes')
else:
    print('No')

for x, y in book.items():
    print(x, y)

for x in book.values():
    print(x)
    
for x in book.keys():
    print(x)