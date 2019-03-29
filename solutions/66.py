print('Введите букву')
b = str(input())
if b == 'm':
    print('q')
else:
    a = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    print(a[a.index(b) + 1])
