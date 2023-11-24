import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split()) #지도 크기 nxm, 주사위 위치(x,y), 명령 개수 k
graph = list(list(map(int, input().split())) for _ in range(n)) #지도
move = list(map(int, input().split())) #명령 입력
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0] #동, 서, 북, 남

dice = [0, 0, 0, 0, 0, 0] #모든 면에 0이 쓰여있음
#최상단은 0, 바닥은 5

def moving_dice(n):
    global dice
    if n == 1: #동쪽으로 이동하면
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif n == 2: #서
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif n == 3: #북
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif n == 4: #남
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]


for moving in move:
    nx = x + dx[moving]
    ny = y + dy[moving] #새로운 좌표
    if 0 <= nx < n and 0 <= ny < m: #세로와 가로안에 있으면
        moving_dice(moving)
        if graph[nx][ny] == 0: #이동한 칸에 0이 있으면
            graph[nx][ny] = dice[5] #주사위 바닥면에 있는 수가 복사
        else: #graph가 0이 아니면
            dice[5] = graph[nx][ny] #쓰여있는 수가 바닥면으로 복사
            graph[nx][ny] = 0 #칸에 있는 수는 0
        print(dice[0]) #윗면에 쓰여있는 수 출력
        x, y = nx, ny #새로운 좌표로 이동
    else:
        continue