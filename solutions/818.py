print('Введите количество проводников')
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = sum(a)
print('ответ на задачу:',b - (n - 1))
