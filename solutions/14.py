print('Введите количество ягод')
a = []
for i in range(3):
	a.append(int(input()))
if a[0] + a[1] > a[2] :
	print(a[0] + a[1] - a[2], 'ягод(ы)')
else:
	print('Impossible')