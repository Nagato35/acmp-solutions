print('Введите число строк и номер строки')
a = int(input())
b = int(input())
if b < a:
    print('1', b)
elif b > a:
    if b - a > a:
        print((b // a) + 1 , b - a - a)
    else:
        print((b // a) + 1 , b - a )
else:
    print('1', a)
