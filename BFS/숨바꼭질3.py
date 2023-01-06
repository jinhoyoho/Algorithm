from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split()) #위치 입력

graph = [-1] * (100001) #0~10만 index를 사용하기 위한 graph list
graph[n] = 0 #현재 시간 0초 저장

q = deque()
q.append(n) #위치 저장

#BFS
while q:
    x = q.popleft() #현재 위치
    
    nx = x - 1 #-1이동
    if 0 <= nx <= 100000 and graph[nx] == -1: #nx가 범위 안에 있고 방문한 적이 없다면
        graph[nx] = graph[x] + 1
        q.append(nx)    

    nx = x * 2 #2배 이동 -> +1보다 더 높은 우선 순위
    if 0 < nx <= 100000 and graph[nx] == -1: #nx가 범위 안에 있고 방문한 적이 없다면
        graph[nx] = graph[x]
        q.append(nx)

    nx = x + 1 #1이동
    if 0 <= nx <= 100000 and graph[nx] == -1: #nx가 범위 안에 있고 방문한 적이 없다면
        graph[nx] = graph[x] + 1
        q.append(nx)

print(graph[k])