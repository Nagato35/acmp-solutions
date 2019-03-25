print('Введите сначала 4 результата 1 команды, затем второй')
a = []
for i in range(8):
	a.append(int(input()))
if a[0] + a[1] + a[2] + a[3] > a[4] + a[5] + a[6] + a[7] :
	print('1')
elif a[0] + a[1] + a[2] + a[3] < a[4] + a[5] + a[6] + a[7] :
	print('2')
else:
	print('DRAW')