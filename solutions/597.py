print("Введите размеры поля и НЛО")
a = []
for i in range(3):
	a.append(int(input()))
if a[2] + a[1] <= a[0]:
	print('Журналисты правы')
else:
	print('Журналисты вруны')