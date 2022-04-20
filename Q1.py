# [1, 2, 3, 4] 隨機排列(不能重複)出3位數，有多少組合?並且print出結果



for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(i, j ,k)