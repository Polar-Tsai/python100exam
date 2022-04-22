# 题目：打印出所有的"水仙花数"，
# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

# x, y, z = 1, 0, 0

# for i in range(100, 1000):
#     flower = x**3 + y**3 + z**3
#     integer = x*100 + y*10 + z*1
#     flower = integer
#     print(flower)
#     break

# 解答
for n in range(100,1000):
    i = n // 100
    j = n // 10 % 10
    k = n % 10
    if n == i*i*i + j*j*j + k*k*k: 
        print(n)


# 153
for n in range(100, 1000): # 三位數，所以限制在100~999之間
    hundred = n // 100
    ten = n // 10 % 10
    single = n % 10
    if n == hundred**3 + ten**3 + single**3:
        print(n)


