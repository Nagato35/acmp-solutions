print('Введите размеры и координаты цифры ')
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a > c and b > d and a > 0 and b > 0 and c > 0 and d > 0:
    if c % 2 == 0:
        print('Эта цифра:',b * c - d)
    elif c % 2 == 1:
        print('Эта цифра:',(b * (c - 1)) - (d - 1))
else:
  print('Durachok')
