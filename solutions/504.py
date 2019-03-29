print('Введите количество дней')
n = int(input())
a = ['G', 'C', 'V']
for i in range(n):
    a[0], a[1], a[2] = a[2], a[0], a[1]
print(a)
