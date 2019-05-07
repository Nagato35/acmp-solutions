print('Введите массы арбузов')
a = []
for i in range(int(input())):
    a.append(int(input()))
print('Теще -',min(a),', себе - ', max(a))
