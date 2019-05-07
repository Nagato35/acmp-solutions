print('Введите координаты клетки')
a = input()
b = int(input())
if (a == 'A' or a == 'C' or a == 'E' or a == 'G') and (b == 1 or b == 3 or b == 5 or b == 7):
    print('BLACK')
else:
    print('WHITE')
