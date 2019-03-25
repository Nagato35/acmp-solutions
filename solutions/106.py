print('Введите количество монеток, а затем их положение')
a = []
for i in range(int(input())):
	a.append(int(input()))
g = 0
r = 0
for i in a:
	if i == 0:
		g = g + 1
	elif i == 1:
		r = r + 1
if g < r:
	print('Нужно перевернуть',g,'монет(у, ы)')
else:
	print('Нужно перевернуть ',r,'монет(у, ы)')