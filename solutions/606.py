import math
print('Введите значения  сторон треугольника')
a = []
for i in range(3):
    a.append(int(input()))
if a[0] < a[1] + a[2] and a[0] > math.fabs(a[2] - a[1]):
    print('YES')
elif a[1] < a[2] + a[0] and a[1] > math.fabs(a[2] - a[0]):
    print('YES')
elif a[2] < a[1] + a[0] and a[2] > math.fabs(a[0] - a[1]):
    print('YES')
else:
    print('NO')
