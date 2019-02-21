# 常识运行
try:
    print('请输入你的手机号')
    # 识别是否全数字
    a = int(input())
    # 转换字符计算数量
    c = str(a)
    b = len(c)
    # 判断手机号尾数是否通过
    if len(c) == 11:
        print('号码验证通过')
    else:
        print('改号码不存在')
except ValueError:
    print('请输入正确的手机号码')
