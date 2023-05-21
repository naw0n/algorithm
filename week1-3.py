# boj15650
# https://www.acmicpc.net/problem/15650

N,M = map(int, input().split())
tmp = []

def dfs(start):
    # success
    if len(tmp) == M:
        print(' '.join(map(str,tmp)))
        return

    for i in range(start, N+1):
        if i not in tmp:
            tmp.append(i)
            dfs(i+1)
            tmp.pop()
dfs(1)