# 주사위 굴리기
import sys
sys.stdin = open("limsumin/백준/input.txt","rt")

dxs = [0, 0, 0, -1, 1]
dys = [0, 1, -1, 0, 0]

# 위, 뒤, 오, 왼, 앞, 바닥 기준으로 정렬 => 상하좌우 turn...
def turn(dir_arr, direction):
    new_arr = []
    if direction == 1: # 동
        new_arr.append(dir_arr[3])
        new_arr.append(dir_arr[1])
        new_arr.append(dir_arr[0])
        new_arr.append(dir_arr[5])
        new_arr.append(dir_arr[4])
        new_arr.append(dir_arr[2])
    if direction == 2: # 서
        new_arr.append(dir_arr[2])
        new_arr.append(dir_arr[1])
        new_arr.append(dir_arr[5])
        new_arr.append(dir_arr[0])
        new_arr.append(dir_arr[4])
        new_arr.append(dir_arr[3])
    if direction == 3: # 북
        new_arr.append(dir_arr[4])
        new_arr.append(dir_arr[0])
        new_arr.append(dir_arr[2])
        new_arr.append(dir_arr[3])
        new_arr.append(dir_arr[5])
        new_arr.append(dir_arr[1])
    if direction == 4: # 남
        new_arr.append(dir_arr[1])
        new_arr.append(dir_arr[5])
        new_arr.append(dir_arr[2])
        new_arr.append(dir_arr[3])
        new_arr.append(dir_arr[0])
        new_arr.append(dir_arr[4])

    return new_arr

dir_arr = [0, 0, 0, 0, 0, 0] # 초기 주사위 배열

n, m, x, y, k = map(int, input().split())

arr = [[0] * m for _ in range(n)]

for i in range(n):
    val_lst = list(map(int, input().split()))
    for j in range(m):
        arr[i][j] = val_lst[j]

# 방향
steps = list(map(int, input().split()))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

cur_x, cur_y = x, y
d = 1 # 동쪽부터 시작
for step in steps:
    d = step
    nx, ny = cur_x + dxs[d], cur_y + dys[d]

    if in_range(nx, ny):
        dir_arr = turn(dir_arr, d)
        if arr[nx][ny] == 0:
            arr[nx][ny] = dir_arr[5]
        else:
            dir_arr[5] = arr[nx][ny]
            arr[nx][ny] = 0
        cur_x, cur_y = nx, ny 

        print(dir_arr[0])