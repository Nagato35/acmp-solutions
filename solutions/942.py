print('Введите количество задач, а затем минут')
a = []
b = []
for i in range(int(input())):
	a.append(int(input()))

sum = 0
wtraf = 0
for number in a:
	sum = sum + number + wtraf
	wtraf = wtraf + number
b.append(sum)

a.reverse()
sum2 = 0
wtraf2 = 0
for number in a:
	sum2 = sum2 + number + wtraf2
	wtraf2 = wtraf2 + number
b.append(sum2)

a.sort()
sum3 = 0
wtraf3 = 0
for number in a:
	sum3 = sum3 + number + wtraf3
	wtraf3 = wtraf3 + number
b.append(sum3)


if b.index(min(b)) == 0:
	print("Выиграл пятикурсник")
elif b.index(min(b)) == 1:
	print("Выиграл третькурсник")
else:
	print("Выиграл первокурсник")