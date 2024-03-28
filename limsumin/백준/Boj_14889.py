# 스타트와 링크
import sys
sys.stdin = open("limsumin/백준/input.txt","rt")

n = int(input())
scores = [
    list(map(int, input().split()))
    for _ in range(n)
]

members = [i for i in range(n)] # 0 ~ n-1 번의 맴버
selected_members = []

def calc_val(lst):
    ans = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            ans += (scores[lst[i]][lst[j]] + scores[lst[j]][lst[i]])

    return ans

def calc():
    others = list(set(members) - set(selected_members))
    # print(selected_members, others)

    selected_ans = calc_val(selected_members)
    other_ans = calc_val(others)
    # print(selected_ans, other_ans)
    return abs(selected_ans - other_ans)

res = int(1e9)

def dfs(idx):
    global res
    if len(selected_members) == n // 2:
        # print(selected_members)
        res = min(res, calc())
        return 
    
    if idx >= n:
        return 
    
    dfs(idx + 1)

    selected_members.append(members[idx])
    dfs(idx + 1)
    selected_members.pop()

dfs(0)
print(res)