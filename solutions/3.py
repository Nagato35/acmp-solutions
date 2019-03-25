print('Введите число которое хотите возвести в квадрат')
a = str(input())
if a[len(a) - 1] == '5':
	if a != '5':
		b = (a[:len(a) - 1])
		c = int(b)
		d = c * (c + 1)
		e = str(d)
		f = str(25)
		print('Квадрат заданного  числа равен :', e + f)
	else:
		print('25')
else:
	print('Ты ввел число не кратное 5')