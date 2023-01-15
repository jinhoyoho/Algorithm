import sys
input = sys.stdin.readline

n, l = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))
visited = [[False] * n for _ in range(n)] #경사로를 두었는지
result = 0 #지나갈 수 있는 길의 개수

#가로부터 확인
for i in range(n):
    token = True #길을 갈 수 있는지 확인
    for j in range(n-1):
        if not token: #길을 갈 수 없다면
            break

        current = graph[i][j] #현재 값
        next = graph[i][j+1] #다음 값
        
        if current == next: #값이 같다면
            continue #pass
        elif current - next == 1: #current가 더 크다면
            if 0 <= j + l < n: #경사로를 놓을 수 있다면
                for k in range(j+1, j+l+1):
                    if graph[i][k] != next: #길이가 같아서 놓을 수 있음
                        token = False
                        break

                    if not visited[i][k]: #경사로를 놓을 수 있다면
                        visited[i][k] = True #경사로를 놓음
                    else: #이미 놓아져있음
                        token = False
                        break
                
                j = j + l #경사로를 놓을 수 있으므로 점프하기
                continue
            else:
                token = False
                break

        elif current - next == -1: #next가 더 크다면
            if 0 <= j + 1 - l < n: #경사로를 놓을 수 있다면
                for k in range(j, j-l, -1): #j부터 j-1+1까지
                    if graph[i][k] != current:
                        token = False
                        break

                    if not visited[i][k]: #경사로를 놓을 수 있다면
                        visited[i][k] = True
                    else: #놓을 수 없다면
                        token = False
                        break
                continue
            else:
                token = False
                break
        else: #1이상 차이가 난다면
            token = False
            break

    if token:
        result += 1

visited = [[False] * n for _ in range(n)] #경사로를 두었는지 (다시 초기화)
#세로 확인
for j in range(n):
    token = True #길을 갈 수 있는지 확인
    for i in range(n-1):
        if not token: #길을 갈 수 없다면
            break

        current = graph[i][j] #현재 값
        next = graph[i+1][j] #다음 값
        
        if current == next: #값이 같다면
            continue #pass
        elif current - next == 1: #current가 더 크다면
            if 0 <= i + l < n: #경사로를 놓을 수 있다면
                for k in range(i+1, i+l+1):
                    if graph[k][j] != next: #길이가 같아서 놓을 수 있음
                        token = False
                        break

                    if not visited[k][j]: #경사로를 놓을 수 있다면
                        visited[k][j] = True #경사로를 놓음
                    else: #이미 놓아져있음
                        token = False
                        break
                
                i = i + l #경사로를 놓을 수 있으므로 점프하기
                continue
            else:
                token = False
                break

        elif current - next == -1: #next가 더 크다면
            if 0 <= i + 1 - l < n: #경사로를 놓을 수 있다면
                for k in range(i, i-l, -1): #i부터 i-1+1까지
                    if graph[k][j] != current:
                        token = False
                        break

                    if not visited[k][j]: #경사로를 놓을 수 있다면
                        visited[k][j] = True
                    else: #놓을 수 없다면
                        token = False
                        break
                continue
            else:
                token = False
                break
        else: #1이상 차이가 난다면
            token = False
            break

    if token:
        result += 1

print(result)