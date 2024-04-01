import sys
sys.stdin = open("limsumin/백준/input.txt","rt")

from collections import deque

n = int(input())
arr = [i for i in range(1, n+1)]
q = deque(arr)

while True:
    if len(q) == 1:
        print(q[0])
        break
    else:
        q.popleft()
        first = q.popleft()
        q.append(first)

