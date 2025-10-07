import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 늘리기 (중요!)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX < rootY:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0: # 합치기 연산
        union(a, b)
    elif op == 1: # 같은 팀인지 확인하는 연산
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")