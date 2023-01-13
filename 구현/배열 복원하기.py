import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
new_size_h = h+x
new_size_w = w+y

array_a = [[0] * w for _ in range(h)]
array_b = [list(map(int, input().split()))for _ in range(new_size_h)]

for i in range(h):
    for j in range(w):
        array_a[i][j] = array_b[i][j] #i, j번째 복사

for i in range(x, h):
    for j in range(y, w):
        array_a[i][j] -= array_a[i-x][j-y] #겹치는 부분 빼기
    
for i in range(h):
    print(*array_a[i])