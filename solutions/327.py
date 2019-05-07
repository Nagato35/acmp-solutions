print('Введите номер билета')
a = []
for i in range(6):
    a.append(int(input()))
if (a[0] + a[1] + a[2] + 1 == a[3] + a[4] + a[5]) or (a[0] + a[1] + a[2] - 1 == a[3] + a[4] + a[5]):
    print('Yes')
else:
    print('No')
