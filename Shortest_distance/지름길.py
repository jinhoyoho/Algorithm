import heapq
import sys

input = sys.stdin.readline


def dijkstra(start):
    pq = []  # 우선순위 큐
    # 시작 노드와 거리 입력
    heapq.heappush(pq, (start, 0))
    distance[start] = 0  # 시작 거리는 0

    while pq:  # 빌때 까지 반복
        curr, dist = heapq.heappop(pq)

        # 최단 거리가 아니라면
        if dist > distance[curr]:
            continue

        for node in graph[curr]:
            cost = dist + node[1]  # 현재까지 거리와 연결된 노드의 거리를 더함
            if cost < distance[node[0]]:  # 현재까지 거리와 연결된 노드의 거리가 최단 거리라면
                distance[node[0]] = cost  # 최단 거리 갱신
                heapq.heappush(pq, (node[0], cost))  # 우선순위 큐 저장


INF = int(1e9)
# 지름길의 개수와 고속도로 길이 입력
n, d = map(int, input().split())

graph = [[] for _ in range(d + 1)]  # 0부터 n까지 그래프 생성
distance = [INF] * (d + 1)  # 거리 저장 리스트 생성

for i in range(d):
    # 다음 노드와 지름길 길이 저장
    graph[i].append((i + 1, 1))

for _ in range(n):
    # 시작 위치, 도착 위치, 지름길 길이 입력
    start, end, shortcut = map(int, input().split())

    if d < end:  # 넘어버리면 의미없음
        continue

    # 저장
    graph[start].append((end, shortcut))

dijkstra(0)
print(distance[d])
