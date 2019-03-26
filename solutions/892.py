print("Введите номер месяца")
a = int(input())
if a >= 1 and a <= 2 :
	print('winter')
elif a == 12:
	print('winter')
elif a >= 3 and a <= 5:
	print('spring')
elif a >= 6 and a <= 8:
	print('summer')
elif a >= 9 and a <= 11:
	print('autumn')
else:
	print('Error')