list = []
count = 0
for i in range(100, 201):
    a = 2
    b = 1
    for j in range(2, i):
        if i % j == 0:
            b = 0
            break
    if b == 1:
        list.append(i)
        count = count + 1

print('质数是', list)
print('数量为', count)
