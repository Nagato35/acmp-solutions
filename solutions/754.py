print('Введите три массы')
a = []
for i in range(3):
	a.append(int(input()))
if (a[0] < 97 or a[0] > 727) or (a[1] < 97 or a[1] > 727) or (a[2] < 97 or a[2] > 727) :
	print('Error')
else:
	print('Наибольшая масса', (max(a)))
