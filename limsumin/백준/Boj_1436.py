# 1로 만들기

import sys
sys.stdin = open("limsumin/백준/input.txt","rt")

n = int(input())
INF = int(1e9)
dp = [INF] * (n + 1)

dp[1] = 0


for i in range(2, n+ 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])