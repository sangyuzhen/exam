# python3
i = 0
list = []
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if a != b != c:
                A = (a * 100 + b * 10 + c)
                i += 1
                list.append(A)
print(list)
print("一共有" + str(i) + "种排列")
