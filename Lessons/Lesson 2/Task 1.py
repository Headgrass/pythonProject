# Напишите программу, которая по заданному номеру четверти показывает диапозон возможных координат точек в этой четверти (x и y)

x = int(input("Enter number of quadrant from 1(ONE) to 4(FOUR): "))

if x == 1:
    print("Range Y: is from 0 to pos.infinit; range X is from 0 to pos.infinit")
elif x == 2:
    print("Range Y: is from 0 to pos.infinit; range X is from 0 to neg.infinit")
elif x == 3:
    print("Range Y: is from 0 to neg.infinit; range X is from 0 to neg.infinit")
elif x == 4:
    print("Range Y: is from 0 to neg.infinit; range X is from 0 to pos.infinit")
else:
    print("Value must be from 1(ONE) to 4(FOUR)")
