# 費式數列
# 0, 1, 1, 2, 3, ...., 144

def fi(n):
    a, b = 0, 1
    for n in range(n-1):
        a = b
        b = a + b
    return a, b

print(fi(10))

# def fib(n):
#     a,b = 1,1
#     for i in range(n-1):
#         a,b = b,a+b
#     return a
