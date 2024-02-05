# https://www.acmicpc.net/problem/2146
# 다리 만들기 
# 두 번의 bfs 사용

import sys
from collections import deque

sys.stdin = open("limsumin/백준/input.txt","rt")

N = int(input())
graph = []
visited = [[0] * N for _ in range(N)]
num = 1
res = int(1e9)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    graph.append(list(map(int, input().split())))

def bfs(a, b):
    queue = deque()
    queue.append([a, b])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] or graph[nx][ny] == 0: 
                continue
            else:
                visited[nx][ny] = 1
                graph[nx][ny] = num
                queue.append([nx, ny])


def cal_min(v):
    queue = deque()
    dist = [[-1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == v:
                dist[i][j] = 0
                queue.append([i, j])
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] and graph[nx][ny] != v:
                    return dist[x][y]
                elif graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append([nx, ny])
    return int(1e9)

for i in range(N):
    for j in range(N):
        if graph[i][j] and not visited[i][j]:
            visited[i][j] = 1
            graph[i][j] = num
            bfs(i, j)
            num += 1

for i in range(1, num):
    res = min(res, cal_min(i))

print(res)