import random

# 创建需要变量
a = 'abcde'
s = []
A = 0
B = 0
C = 0
D = 0
E = 0
gm = {}
# 生成1000个字母
for i in range(1000):
    b = random.choice(a)
    s.append(b)
for j in range(len(s)):
    if s[j] == 'a':
        A = A + 1
    elif s[j] == 'b':
        B = B + 1
    elif s[j] == 'c':
        C = C + 1
    elif s[j] == 'd':
        D = D + 1
    elif s[j] == 'e':
        E = E + 1
# 结果添加到字典
gm.setdefault("A", A)
gm.setdefault("B", B)
gm.setdefault("C", C)
gm.setdefault("D", D)
gm.setdefault("E", E)
# 输出结果
print('共', len(s), '字母')
print(gm)
