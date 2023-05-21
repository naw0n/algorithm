# boj27930
# https://www.acmicpc.net/problem/27930

yonsei = ['Y','O','N','S','E','I']
korea = ['K','O','R','E','A']
yNum, kNum = 0

input = str(input())
element = list(input)

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