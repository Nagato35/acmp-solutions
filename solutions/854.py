print('Введите данные ')
a = int(input())
b = int(input())
c = str(input())
if b > a and (c == 'auto' or c == 'heat') :
    print(b)
elif b < a and (c == 'auto' or c == 'freeze'):
    print(b)
elif b == a or (c == 'auto' or c == 'freeze' or c == 'heat' or c == 'fan'):
    print(b)
else :
    print(a)
