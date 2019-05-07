a = []
for i in range(6):
    a.append(int(input()))
b = abs((a[2] - a[0]) * (a[2] - a[0]) + (a[3] - a[1]) * (a[3] - a[1]))
c = abs((a[4] - a[0]) * (a[4] - a[0]) + (a[5] - a[1]) * (a[5] - a[1]))
d = abs((a[4] - a[2]) * (a[4] - a[2]) + (a[5] - a[3]) * (a[5] - a[3]))
s = abs(((b + c + d)/3) * ((b + c + d)/3 - a) * ((b + c + d)/3 - b) * ((b + c + d)/3 - d))
print(s)
