# 判断101-200之间有多少个素数，并输出所有素数
a = []
b = []
for i in range(100, 201):
    for j in range(2, i):
        if i % j == 0:
            a.append(i)
            break
        else:
            b.append(i)
            break
print('素数有L', a)
print('不是素数的有', b)
