import random

field = []
def print_field(field_print):
    for i in range(3):
        print("  ".join(field_print[i]))

def player_move (field_print):
    move = input("Введите кооржинаты вашего входа через запятую: ")
    move_coord = move.split(',')
    x = int(move_coord[0])
    y = int(move_coord[1])
    field[x][y] = 'X'
    return field_print

def comp_move (field_print):
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    while field[x][y] != '_':
        x = random.randint(0, 2)
        y = random.randint(0, 2)
    field[x][y] = '0'
    return field_print

for i in range(3):
    fieldrow = []
    for j in range(3):fieldrow.append('_')
    field.append(fieldrow)
print_field(field)

for m in range(9):
    if m%2==0: field = player_move(field)
    else: field = comp_move(field)
    print_field(field)
