print('Введите часы когда вы ложитесь спать и когда намерены встать')
i = []
i = input().split()
if int(i[1]) > int(i[0]) :
    print(int(i[1]) - int(i[0]), 'часов(а)')
elif (int(i[1]) == int(i[0])) :
    print('12 часов(а)')
else:
    print(12 - (int(i[0]) - int(i[1])), 'часов(а)')
