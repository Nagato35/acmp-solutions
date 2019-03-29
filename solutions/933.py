print('Введите лимит разговора и плату за 1 минуту')
a = []
for i in range(4):
    a.append(int(input()))
if a[3] <= a[0]:
    print(a[0] * a[1])
else:
    print((a[0] * a[1]) + ((a[3] - a[0]) * a[2]))
