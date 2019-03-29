print('Введите числа конечных автоматов\n')
n = int(input())
a = []
b = []
l = []
print('Введите число состояний и переходов\n')
for i in range(n):
    l = input().split()
    a.append(int(l[0]))
    b.append(int(l[1]))
    l = []
for i in range(0 , len(a)):
    d = 19 * b[i] + (a[i] + 239)*(a[i] + 366) / 2
    print(d)
