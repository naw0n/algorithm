# boj27930
# https://www.acmicpc.net/problem/27930

yonsei = "YONSEI"
korea = "KOREA"

yNum = 0
kNum = 0

for i in input():
    if yonsei[yNum] == i: 
        yNum += 1
        if yNum == 6:
            print(yonsei)
            exit()
    if korea[kNum] == i:
        kNum += 1
        if kNum == 5:
            print(korea)
            exit()