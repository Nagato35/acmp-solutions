print('Введите номер года нашей эры.')
a = int(input())
if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0) :
    print('12 / 09 /',a)
else:
    print('13 / 09 /',a)
