# https://www.acmicpc.net/problem/14501
# 퇴사

import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

N = int(input())

t_list = []
p_list = []

for _ in range(N):
    t, p = map(int, input().split())

    t_list.append(t)
    p_list.append(p)


dp = [0] * (N+1)

for i in range(N):
    if i + t_list[i] < N+1:
        dp[i+ t_list[i]] = max(dp[i+ t_list[i]], dp[i] + p_list[i])
    dp[i + 1] = max(dp[i], dp[i + 1])

print(dp[-1])