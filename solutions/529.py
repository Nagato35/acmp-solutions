import math
a = []
for i in range(4):
    a.append(int(input()))
c = math.sqrt(((a[2] - a[0])**2 + (a[3] - a[1])**2))
print(c)
