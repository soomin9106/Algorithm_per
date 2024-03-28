# 연구소 3
# 0은 빈 칸, 1은 벽, 2는 비활성 바이러스
# 활성화 할 바이러스 M 개를 골라서 바이러스가 전체에 퍼지는 최소시간 구하기
# 바이러스를 어떻게 놓아도 빈칸인 경우 => arr[x][y] == 0 인데 , visited 는 안차있는 경우

import sys
sys.stdin = open("limsumin/백준/input.txt","rt")

from collections import deque

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]


# 비활성화 바이러스 위치들
viruses = []
selected_viruses = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            viruses.append((i, j))
viruses_cnt = len(viruses)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    q = deque()
    visited = [[False] * n for _ in range(n)]
    seconds = [[0] * n for _ in range(n)]
    for sv in selected_viruses:
        x, y = sv
        q.append((x, y, 0))
        visited[x][y] = True

    while q:
        cur_x, cur_y, cur_cnt = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy

            if in_range(nx, ny) and not visited[nx][ny] and arr[nx][ny] == 0: # 빈칸인 경우
                q.append((nx, ny, cur_cnt + 1))
                visited[nx][ny] = True
                seconds[nx][ny] = cur_cnt + 1
            if in_range(nx, ny) and not visited[nx][ny] and arr[nx][ny] == 2: # 비활성화였던 바이러스
                q.append((nx, ny, cur_cnt + 1))
                visited[nx][ny] = True
                # seconds[nx][ny] = cur_cnt + 1


    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0 and not visited[i][j]: # 빈칸인데 방문하지 못한 경우
                return -1
    
    ans = -int(1e9)

    for second in seconds:
        val = max(second)
        ans = max(ans, val)

    return ans

answer = int(1e9)

def choose_viruses(idx):
    global answer
    if len(selected_viruses) == m:
        # bfs 수행 
        cur_ans = bfs()
        if cur_ans == -1:
            return
        answer = min(answer, cur_ans)
        return
    
    if idx >= viruses_cnt:
        return 
    
    choose_viruses(idx + 1)

    selected_viruses.append(viruses[idx])
    choose_viruses(idx + 1)
    selected_viruses.pop()

choose_viruses(0)

if answer == int(1e9):
    print(-1)
    exit(0)
print(answer)