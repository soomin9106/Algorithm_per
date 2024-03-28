import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

import heapq

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    val = int(sys.stdin.readline())

    if val != 0: # val 을 넣는 연산
        heapq.heappush(arr, (abs(val), val))

    if val == 0:
        if len(arr) == 0:
            print(0)
        else:
            res = heapq.heappop(arr)
            print(res[1])