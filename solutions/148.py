print('Введите числа ')
a = []
for i in range(2):
    a.append(int(input()))
c = (max(a) + 1)
for i in range(1, c):
    if a[0] % i == 0 and a[1] % i == 0 :
        d = i
        q = []
        for i in range(1):
            q.append(d)
print('НОД:',max(q))
