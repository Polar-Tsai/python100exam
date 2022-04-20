# 题目：将一个列表的数据复制到另一个列表中。

# solution 
list_a = [5, 9, 8]
list_b = []
for i in range(len(list_a)):
    list_b.append(list_a[i])
print(list_b)

# solution 2
list_c = list_a[:]
print(list_c)