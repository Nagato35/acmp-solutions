print('Введите количество чисел')
a = []
for i in range(int(input())):
	a.append(int(input()))
a.reverse()
print(a)