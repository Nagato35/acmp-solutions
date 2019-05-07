a = []
for i in range((2 * int(input()))):
    a.append(int(input()))
if 1 in a:
    c = a.index(max(a))
    if a[c + 1] == 1:
        print(c)
    else:
        del a[c]
        s = a.index(max(a))
        if a[s + 1] == 1:
            print(s)
else:
    print('-1')
