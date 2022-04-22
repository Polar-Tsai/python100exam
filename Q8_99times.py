# 製作9*9乘法表

for i in range(1, 10):
    print()
    for j in range(1, 10):
        sum = i * j
        print("{} x {} = {}".format(j, i, sum), end="   ")
