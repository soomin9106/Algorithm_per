import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))


stack = []
operators = []
arr_idx = 0 

for i in range(1, n + 1):
    stack.append(i)
    operators.append('+')
    if arr[arr_idx] == i: # pop 해야 하는 상황
        stack.pop()
        operators.append('-')
        arr_idx += 1
        while arr_idx < len(arr):
            if not stack:
                break
            if arr[arr_idx] != stack[-1]:
                break  
            else:
                stack.pop()
                operators.append('-')
                arr_idx += 1

if len(stack) >= 1:
    print("NO")
    exit(0)

for o in operators:
    print(o)
