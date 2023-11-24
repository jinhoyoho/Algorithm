import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1] #(dy, dx)

n = int(input()) #커브의 개수
result = [[0] * 101 for _ in range(101)] #100x100사이즈
for _ in range(n): #n개만큼 반복
    x, y, d, g = map(int, input().split()) #x, y좌표와 방향, 세대 입력
    result[x][y] = 1 #지나가면 1로 변경
    
    move = [d] #움직이는 방향
    for i in range(g): #세대만큼 반복
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i - 1] + 1) % 4) #move배열에서 1씩 더한 것
        move.extend(tmp) #뒤에 붙이기
    
    for direction in move:
        nx = x + dx[direction]
        ny = y + dy[direction]
        result[nx][ny] = 1
        x, y = nx, ny

count = 0
for i in range(100):
    for j in range(100):
        if result[i][j] and result[i+1][j] and result[i][j+1] and result[i+1][j+1]:
            count += 1

print(count)