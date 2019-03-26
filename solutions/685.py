print('Введите значения цен и количество килограмм в горшках')
a = []
for i in range(3):
	a.append(int(input()))
a.sort()
b = []
for n in range(3):
	b.append(int(input()))
b.sort()
c = (a[0] * b[0]) + (a[1] * b[1]) + (a[2] * b[2])
print('Они заработают ', c, 'монет')