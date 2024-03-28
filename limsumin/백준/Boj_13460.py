# 구슬 탈출 2

from collections import deque
import sys
sys.stdin = open("limsumin/백준/input.txt","rt")

from collections import deque

n, m = map(int, input().split())

maps = []
rx, ry = 0, 0
bx, by = 0, 0

for i in range(n):
    s = input()
    temp = []
    for j in range(m):
        temp.append(s[j])
        if s[j] == 'R':
            rx, ry = i, j
        elif s[j] == 'B':
            bx, by = i, j
    maps.append(temp)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

def move(x, y, i, j):
    count = 0
    while maps[x + i][y + j] != '#' and maps[x][y] != 'O': # 다음 이동 장소는 벽이 아니고, 나 자신은 구멍이 아니어야 함
        x += i
        y += j
        count += 1

    return x, y, count

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by, 1))
    visited = []
    visited.append((rx, ry, bx, by))

    while q:
        cur_rx, cur_ry, cur_bx, cur_by, cnt = q.popleft()

        if cnt > 10:
            break

        for dx, dy in zip(dxs, dys):
            nrx, nry, nrcnt = move(cur_rx, cur_ry, dx, dy)
            nbx, nby, nbcnt = move(cur_bx, cur_by, dx, dy)

            if maps[nbx][nby] == 'O':
                continue

            if maps[nrx][nry] == 'O':
                return cnt
            
            if nrx == nbx and nry == nby:
                if nrcnt > nbcnt:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy
            if (nrx, nry, nbx, nby) not in visited:
                visited.append((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, cnt + 1))

    return -1

print(bfs(rx, ry, bx, by))