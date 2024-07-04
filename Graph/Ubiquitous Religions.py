import sys
input = sys.stdin.readline


def dfs(point, graph, visited):
    visited[point] = True

    for node in graph[point]:
        if visited[node] == False:
            dfs(node, graph, visited)

    return True


case = 0

while True:
    case += 1
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    count = 0

    visited = [False for _ in range(n+1)]

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    for i in range(1, n+1):
        if visited[i] == False:
            count += 1
            dfs(i, graph, visited)

    print(f"Case {case}:", count)
