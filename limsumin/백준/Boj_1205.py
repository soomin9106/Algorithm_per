# 등수 구하기

import sys
sys.stdin = open("limsumin/백준/input.txt","rt")

n, score, p = map(int, input().split())

if n == 0:
    print(1)
    exit(0)
else:
    ranks = list(map(int, input().split()))
    ranks.sort(reverse=True)

    if n == p and ranks[-1] >= score:
        print(-1)
        exit(0)

    else:
        res = n + 1

        for i in range(n):
            if ranks[i] <= score:
                res = i + 1
                break

        print(res)