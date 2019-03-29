n = int(input("Введите кол-во элементов последовательности\n"))
print("Введите последовательность чисел")
a = []
for i in range(n):
    a.append(int(input()))
l = len(a)
m = 2
ms = []
if l % 2 == 0:
    for i in range (2, l, 2):
        if a[i - 2] < a[i - 1] > a[i]:
            m += 1
            if a[i - 1] > a[i] < a[i + 1]:
                m += 1
            else:
                ms.append(m)
                m = 2
        elif a[i - 2] > a[i - 1] < a[i]:
            m += 1
            if a[i - 1] < a[i] > a[i + 1]:
                m += 1
            else:
                ms.append(m)
                m = 2
        else:
            pass
    ms.append(m)
    print(max(ms))
else:
    print ("still in beta")


# k = True
# m = 1
# inc = 2
# for i in range(1, l-1):
#     if a[i - 1] < a[i] > a[i + 1]:
#         m += 1
#         if a[i + 1] > a[i + 2]:
#             while a[i + inc] > a[i + inc + 1]:
#                 inc += 1
#             m +=1
#         else:
#             pass
#     if a[i - 1] > a[i] < a[i + 1]:
#         m += 1
#         if a[i + 1] < a[i + 2]:
#             while a[i + inc] < a[i + inc + 1]:
#                 inc += 1
#             m +=1
#         else:
#             pass
# print(m)

# 5 7 6 3 4 2 7 1 8 9 4 5
