import math
import random

a = []
c = ''
for i in range(20):
    b = random.choice(range(10))
    a.append(b)
print('随机列表', a)
for j in range(0, len(a), 2):
    c = c + str(a[j])
print(math.radians(int(c)))
