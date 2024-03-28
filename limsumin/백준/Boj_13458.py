# 시험 감독

import sys
sys.stdin = open("limsumin/백준/input.txt","rt")

import math

n = int(input())
arr = list(map(int, input().split()))

b, c = map(int, input().split())

ans = 0
for a in arr:
    if b >= a:
        ans += 1
        continue
    else:
        temp = a
        temp -= b
        ans += 1

        ans += math.ceil(temp / c)

print(ans)
