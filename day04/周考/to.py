import random

# 创建正数列表
a = []
c = []
# 随机50个正负数
for i in range(50):
    b = random.choice(range(-10, 10))
    # 分类添加到列表
    if b >= 0:
        a.append(b)
    else:
        c.append(b)
        # 输出
print('正数列表', a)
print('负数列表', c)
