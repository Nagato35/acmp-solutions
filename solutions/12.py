print('Введите 3 натуральных числа')
a = []
for i in range(3):
	a.append(int(input()))
if a[0] * a[1] == a[2] :
	print('YES')
else:
	print('NO')