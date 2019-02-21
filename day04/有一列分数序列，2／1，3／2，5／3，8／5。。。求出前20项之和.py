# 有一列分数序列，2／1，3／2，5／3，8／5。。。求出前20项之和
sum = 0
a = 2
b = 1
list = []
for i in range(20):
    h = str(a) + '/' + str(b)
    list.append(h)
    sum = sum + a / b
    a = a + b
    b = a - b
print(list)
print(sum)
