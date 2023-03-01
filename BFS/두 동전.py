from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #세로, 가로 입력
graph = [[0]*m for _ in range(n)] #nxm크기의 지도 생성
coins = list() #동전 좌표
for i in range(n):
    input_map = input().rstrip() #동전 좌표 입력
    for j in range(m):
        graph[i][j] = input_map[j] #경로 복사
        if input_map[j] == 'o': #동전이라면
            coins.append([i,j]) #동전 좌표 입력

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1] #상하좌우

def bfs():
    q = deque()
    q.append([coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0]) #동전 좌표 입력

    while q:
        x1, y1, x2, y2, count = q.popleft() #좌표, 이동 횟수 출력
        if count >= 10:
            return -1
        
        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i] #새로운 좌표 입력
            
            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m: #좌표 안에 있다면
                if graph[nx1][ny1] == '#': #벽이면
                    nx1, ny1 = x1, y1 #원래 좌표
                if graph[nx2][ny2] == '#': #벽이면
                    nx2, ny2 = x2, y2 #원래 좌표
                q.append([nx1, ny1, nx2, ny2, count+1]) #동전 저장

            elif 0 <= nx1 < n and 0 <= ny1 < m: #coin2가 떨어진 경우
                return count+1 
            elif 0 <= nx2 < n and 0 <= ny2 < m: #coin1이 떨어진 경우
                return count+1
            else: #둘 다 빠진 경우
                continue
    
    return -1

print(bfs())