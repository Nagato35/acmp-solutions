print('Введите сколько C, Н и O – атомов углерода')
a = int(input())
b = int(input())
c = int(input())
if a>=2 and b>=6 and c>=1:
    if (a / 2) == (b / 6) == (c / 1) :
        print(a / 2)
    else:
        d = [a//2 , b//6 , c ]
        print(min(d))
else:
    print(0)
