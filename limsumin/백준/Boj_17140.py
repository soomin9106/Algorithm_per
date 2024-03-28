# 이차원 배열과 연산

import sys
sys.stdin = open("limsumin/백준/input.txt","rt")

from collections import defaultdict

r, c, k = map(int, input().split())
r -= 1
c -= 1

arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))

# 배열 조건에 맞게 바꾸는 함수
def count(oneArr):
    count = defaultdict(int)
    for o in oneArr:
        count[o] += 1
    sorted_cnt = sorted(count.items(), key = lambda x: (x[1], x[0]))
    # print('sorted_cnt', sorted_cnt)
    res = []

    for item in sorted_cnt:
        if item[0] == 0:
            continue
        else:
            res.append(item[0])
            res.append(item[1])

    return res

# 배열 길이 맞춰주기
def adapt_arr(ta):
    max_len = 0
    max_len = min(100, max(len(t) for t in ta))
    res = []

    for t in ta:
        temp_res = []
        if len(t) == max_len:
            res.append(t)
        elif len(t) < max_len:
            for i in range(len(t)):
                temp_res.append(t[i])
            for i in range(max_len - len(t)):
                temp_res.append(0)
            res.append(temp_res)
        else:
            for i in range(100):
                temp_res.append(t[i])
            res.append(temp_res)
    
    return res


# R to C
def reverse_arr(ta):
    new_arr = []

    for i in range(len(ta[0])):
        temp = []
        for j in range(len(ta)):
            temp.append(ta[j][i])
        new_arr.append(temp)

    return new_arr

# R 연산 수행
def r_calculate():
    temp_arr = []
    for i in range(len(arr)):
        temp = count(arr[i])
        temp_arr.append(temp)
    
    res_arr = adapt_arr(temp_arr)
    # print('arr', res_arr)
    return res_arr

# C 연산 수행
def c_calculate():
    temp_arr = []
    for i in range(len(arr[0])):
        col = []
        for j in range(len(arr)):
            col.append(arr[j][i])
        col = count(col)
        # print('col', col)
        temp_arr.append(col)

    res_arr_reversed = adapt_arr(temp_arr)
    res_arr = reverse_arr(res_arr_reversed)
    return res_arr

def in_range(x, y):
    return 0 <= x < len(arr) and 0 <= y < len(arr[0])


res = 0
while True:
    if res>= 101:
        res = -1
        break
    if in_range(r, c) and arr[r][c] == k:
        break
    if len(arr[0]) <= len(arr):
        arr = r_calculate()
    else:
        arr = c_calculate()
    res += 1

print(res)   