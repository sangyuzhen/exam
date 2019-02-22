# 将一个列表的数据复制到另一个列表中，并反向排序输出。
a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
b = []
# 把a 复制到b
for i in range(len(a)):
    b.append(a[i])
print('结果', b)
b = sorted(b, reverse=False)
print('排序后结果是', b)
