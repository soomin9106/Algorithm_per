# 경사로
import sys
sys.stdin = open("limsumin/백준/input.txt","rt")

n, l = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

def in_range(cur):
    return 0 <= cur < n

# 길인지 아닌지 체크
def check(line):
    # 경사로로 썼는지 체크
    visited = [False] * n
    for i in range(0, n - 1):
        # 이전 길이 == 다음 길이: 그냥 넘어감
        if line[i] == line[i + 1]:
            continue

        # 이전 길이와 다음 길이가 1 초과로 차이 나면 길을 만들 수 없음
        elif abs(line[i + 1] - line[i]) > 1:
            return False
        
        # 현재 길이가 다음 길이보다 길 때 (1차이 나는 것은 보장)
        elif line[i] > line[i + 1]:
            temp = line[i + 1]
            for j in range(i + 1, i + l + 1):
                if in_range(j):
                    if temp != line[j]:
                        return False
                    
                    elif visited[j]:
                        return False
                    
                    visited[j] = True
                else:
                    return False
        # 다음 길이가 현재 길이보다 길 때     
        else:
            temp = line[i]
            for j in range(i, i - l, -1):
                if in_range(j):
                    if temp != line[j]:
                        return False
                    elif visited[j]:
                        return False
                    visited[j] = True
                else:
                    return False
                
    return True

answer = 0

for i in range(n):
    if check(arr[i]):
        answer += 1

for j in range(n):
    temp_arr = []

    for i in range(n):
        temp_arr.append(arr[i][j])

    if check(temp_arr):
        answer += 1

print(answer)

