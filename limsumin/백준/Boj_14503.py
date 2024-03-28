# 로봇 청소기
import sys
sys.stdin = open("limsumin/백준/input.txt","rt")

from collections import deque

# 북동남서 순서
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

n, m = map(int, input().split())
x, y, d = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

visited = [[False] * m for _ in range(n)]

visited[x][y] = True
ans = 1

while True:
    not_cleaned = False
    for i in range(4):
        d = 3 if d == 0 else d - 1
        nx, ny = x + dxs[d], y + dys[d]

        if in_range(nx, ny) and maps[nx][ny] == 0 and not visited[nx][ny]:
            not_cleaned = True
            visited[nx][ny] = True
            x, y = nx, ny 
            ans += 1
            break

    if not not_cleaned:
        nx, ny = x - dxs[d], y - dys[d] 
        if maps[nx][ny] == 1:
            print(ans)
            break
        else:
            x, y = nx, ny

    