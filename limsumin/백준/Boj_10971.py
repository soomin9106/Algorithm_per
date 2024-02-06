# https://www.acmicpc.net/problem/10971
# 외판원 순회 2 - 다시 풀어보기

import sys
from collections import defaultdict

sys.stdin = open("limsumin/백준/input.txt","rt")
input = sys.stdin.readline

N = int(input())

graph = defaultdict(list)
cost = int(1e9)
visited = [False] * (N+1)
first = 1

for i in range(1, N+1):
    arr = [0] + list(map(int, input().split()))
    for j in range(1, len(arr)):
        if arr[j] != 0 and i != j:
            graph[i].append([j, arr[j]])


def dfs(start, val, depth = 1):
    global first # 진짜 첫 시작점
    global cost
    global visited
    if depth == N:
        for x, _cost in graph[start]:
            if x == first:
                cost = min(cost, val + _cost)
            return
    
    if not visited[start]:
        visited[start] = True


    for point, we in graph[start]:
        if not visited[point]:
            dfs(point, val + we, depth + 1)
            visited[point] = False


for i in range(1, N+1):
    first = i
    visited = [False] * (N+1)
    dfs(i, 0)

print(cost)