print('Введите количество очков первого игрока')
b = int(input())
c = b * 6
if b % 6 == 5:
    print('MIN:',(b // 6) * 1 + 2,'MAX:', c)
elif b % 6 == 4:
    print('MIN:',(b // 6) * 1 + 3,'MAX:',c)
elif b % 6 == 3:
    print('MIN:',(b // 6) * 1 + 4,'MAX:',c)
elif b % 6 == 2:
    print('MIN:',(b // 6) * 1 + 5,'MAX:',c)
elif b % 6 == 1:
    print('MIN:',(b // 6) * 1 + 6,'MAX:',c)
elif b % 6 == 0:
    print('MIN:',(b // 6) * 1,'MAX:',c)
elif b < 1:
    print('Условие читай внимательнее!!!')
