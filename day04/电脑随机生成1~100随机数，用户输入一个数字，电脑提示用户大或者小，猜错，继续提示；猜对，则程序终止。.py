# 电脑随机生成1~100随机数，用户输入一个数字，电脑提示用户大或者小，猜错，继续提示；猜对，则程序终止。
import random

a = random.choice(range(1, 100))
print(a)
print('请输入1-100的数字')
while 1:
    b = int(input())
    if a == b:
        break
    elif a > b:
        print('输入的数字小了')
    elif a < b:
        print('输入的数大了')
