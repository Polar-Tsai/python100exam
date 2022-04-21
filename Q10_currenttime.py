# 暂停一秒输出，并格式化当前时间。
import time

for i in range(10):
    print(time.asctime())
    time.sleep(1)