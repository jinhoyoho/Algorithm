import sys
import heapq
input = sys.stdin.readline
INF = 1e9


def dijkstra(start):
    distance = [INF for _ in range(n+1)]  # 거리 초기화

    pq = list()
    heapq.heappush(pq, (start, 0))  # 시작과 비용 넣기
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

    return distance


T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())  # 교차로, 도로, 목적지 후보 개수
    s, g, h = map(int, input().split())  # 출발지, g와 h 교차로 사이에 있는 도로로 지나감

    graph = [[] for _ in range(n+1)]
    goal = list()

    for _ in range(m):  # m개의 도로
        a, b, d = map(int, input().split())
        if (a == g and b == h) or (a == h and b == g):
            bridge_cost = d
        graph[a].append((b, d))
        graph[b].append((a, d))

    for _ in range(t):  # t개의 후보
        goal.append(int(input()))

    distFromS = dijkstra(s)
    distFromG = dijkstra(g)
    distFromh = dijkstra(h)

    answer = list()

    for finish in goal:
        if (distFromS[g] + bridge_cost + distFromh[finish] == distFromS[finish]) or (distFromS[h] + bridge_cost + distFromG[finish] == distFromS[finish]):
            answer.append(finish)

    answer.sort()
    print(*answer)
