print('Введите количество мостов, а затем их размеры')
a = []
c = 456
for i in range(int(input())):
    a.append(int(input()))
for i in a:
    if i < 438:
        c = i
        break
if c < 438:
    print('crash', (a.index(c)) + 1)
else:
    print('No crash')
