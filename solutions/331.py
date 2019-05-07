print('Введите время нужное для решения задачи')
a = input()
i = input().split()
e = int(i[0])
f = int(i[1])
s1 = a[0] + a[1]
s2 = a[3] + a[4]
b = int(s1)
c = int(s2)
d = b * 60 + c
g = e * 60 + f
j = d + g
if j > 1440:
    j = j - 1440 * (j // 1440)
    print(j // 60,':',j - 60 * (j // 60))
elif j < 1440:
    print(j // 60,':',j - 60 * (j // 60))
