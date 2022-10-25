# Дан список чисел. Создайте список, в который попадают числа,
# описывающие максимальную сплошную возрастающую последовательность.
# Порядок элементов менять нельзя.
#
# *Пример:*
#
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7] => [1, 5]

def find_list(start_list):
    min_num = min(start_list)
    new_list = [min_num]
    max_num = max(start_list)
    index = [min_num, max_num]

    for i in range(min_num, max_num):
        if min_num + 1 in start_list:
            new_list.append(min_num + 1)
        min_num += 1

    if len(new_list) > 1:
        return new_list, index

    return []

try:
    test = [5, 8, 100, 97, 2, 5, 2, 3, 4, 6, 1, 7, 5, 9]
    current_list = find_list(test)
    print(current_list)

except:
    print("Что-то не работает")

# не смог доделать, так как не понял, как зафикисровать конечный последовательный элемент