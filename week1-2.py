# boj10026
# https://www.acmicpc.net/problem/10026

import sys
from collections import deque

# up, down, left, right
directionX = [-1, 0, 1, 0]
directionY = [0, 1, 0, -1]

def bfs(i, j, rgb, array):
    queue = deque()
    queue.append((i,j))
    array[i][j]=0
    
    while queue:
        x, y = queue.popleft()
        for index in range(4):
            xNum = x + directionX[index]
            yNum = y + directionY[index]
            if xNum < 0 or xNum > n-1 or yNum <0 or yNum > y-1:
                continue
            if array[xNum][yNum] == rgb:
                array[xNum][yNum] = 0
                queue.append((xNum, yNum))
                
n = int (sys.stdin.readline())
# general
general = [list(sys.stdin.readline()) for _ in range(n)] 
# color weakness
colorWeak = [[0] * n for _ in range(n)] 

# color weakness : R, G -> R
for i in range(n):
    for j in range(n):
        if general[i][j] == 'R' or general[i][j] == 'G':
            colorWeak[i][j] = 'R'
        else:
            colorWeak[i][j] = 'B'

colorCount_G = colorCount_W = 0

for i in range(n):
    for j in range(n):
        # general
        if general[i][j] != 0:
            bfs(i,j,general[i][j], general)
            colorCount_G += 1
        # color weakness
        if colorWeak[i][j] != 0:
            bfs(i, j, colorWeak[i][j], colorWeak)
            colorCount_W += 1

print(colorCount_G, colorCount_W)