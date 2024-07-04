import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    pq = list()
    heapq.heappush(pq, (start, 0))
    distance[start] = 0

    while pq:
        curr, dist = heapq.heappop(pq)

        if dist > distance[curr]:
            continue

        for node in graph[curr]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(pq, (node[0], cost))


INF = 1e9

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]

item = list(map(int, input().split()))


for _ in range(r):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

result = 0

for i in range(1, n+1):
    distance = [INF] * (n + 1)  # 거리 저장 리스트 생성

    dijkstra(i)
    count = 0

    for j in range(1, n+1):
        if distance[j] <= m:
            count += item[j-1]

    result = max(result, count)


print(result)
