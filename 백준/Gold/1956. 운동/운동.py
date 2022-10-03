import sys
input = sys.stdin.readline
INF = 9876543210

v, e = map(int, input().split()) #노드와 간선 입력
graph = [[INF] * (v+1) for _ in range(v+1)] #1부터 v까지 INF로 2차원 그래프
for i in range(1, v+1):
    for j in range(1, v+1):
        #자기 자신은 0으로 초기화
        if i == j:
            graph[i][j] = 0

for _ in range(e):
    #a에서 b로 거리c 입력
    a, b, c = map(int, input().split())
    graph[a][b] = c

#플루이드 워셜 알고리즘
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = INF
for i in range(1, v+1):
    for j in range(1, v+1):
        #같은 경우는 제외
        if i == j:
            continue
        #사이클 발생하는 경우 더하기
        result = min(result, graph[i][j] + graph[j][i])

if result >= INF:
    print(-1)
else:
    print(result)