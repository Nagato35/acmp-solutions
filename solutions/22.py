print('Введите число')
a = int(input())
sum = 0
b = a + 1
if a % 2 == 0:
    while (a - 1) % 2 == 1:
        sum = sum + 1
else:
    while a % 2 == 1:
        sum = sum + 1
print(sum)
