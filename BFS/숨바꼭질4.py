from collections import deque
import sys
sys.setrecursionlimit(10*5)
input = sys.stdin.readline

#경로 찾기
def search(node):
    result = list()
    tmp = node

    for _ in range(graph[k]+1): #graph[k](걸린시간) + 1번 반복 -> 자기자신은 0초이므로
        result.append(tmp) #노드 저장
        tmp = prior[tmp]   #tmp 이전 노드 tmp에 저장
    
    result.reverse() #뒤집기
    print(*result)   #출력

n, k = map(int, input().split()) #위치 입력

graph = [-1] * (100001) #0~10만 index를 사용하기 위한 graph list
graph[n] = 0 #현재 시간 0초 저장
prior = [-1] * (100001) #0~10만 이전 노드 저장

q = deque()
q.append(n) #위치 저장
result = [k] #이동 경로 저장

#BFS
while q:
    x = q.popleft() #현재 위치

    if x == k: #도달했다면
        print(graph[k]) #결과 출력
        search(x) #경로 출력
        break

    for i in (x-1, x*2, x+1):
        if 0 <= i <= 100000 and graph[i] == -1: #nx가 범위 안에 있고 방문한 적이 없다면
            graph[i] = graph[x] + 1
            q.append(i)
            prior[i] = x #이전 경로에 현재 x 저장