# https://www.acmicpc.net/problem/9465
# 스티커

import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

T = int(input())

for _ in range(T):
    N = int(input())
    arr = []
    dp = [[0] * (N+1) for _ in range(2)]
    for _ in range(2):
        arr.append([0] + list(map(int, input().split())))

    dp[0][1] = arr[0][1]
    dp[1][1] = arr[1][1]

    for i in range(2, N+1):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i]


    print(max(dp[0][-1], dp[1][-1]))