import math
a = int(input())
b = int(input())
c = int(input())
if abs(b - c) == 1:
    print(1)
else:
    d = []
    d.append(b)
    d.append(c)
    f = []
    f.append(max(d) - min(d))
    f.append(a - max(d))
    print(min(f))
