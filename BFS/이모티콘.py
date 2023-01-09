from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((1, 0)) #(이모티콘 개수, 클립보드 개수)
    graph[1][0] = 0 #시작
    while q:
        x, y = q.popleft()
        if graph[x][x] == -1: 
            graph[x][x] = graph[x][y] + 1 #이모티콘을 클립보드에 복사
            q.append((x,x))
        if x + y <= s and graph[x+y][y] == -1:
            graph[x+y][y] = graph[x][y] + 1 #클립보드에 있는 것 붙여넣기
            q.append((x+y, y))
        if x-1 >= 0 and graph[x-1][y] == -1:
            graph[x-1][y] = graph[x][y] + 1 #현재 이모티콘 삭제
            q.append((x-1, y))    

s = int(input()) #입력할 이모티콘 개수 입력
graph = [[-1] * (s+1) for _ in range(s+1)] #(s, c) -> (이모티콘 개수, 클립보드 개수)
bfs() #bfs
graph[s].sort() #오름차순 정렬
print(graph[s][1]) #결과