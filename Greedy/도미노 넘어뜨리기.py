import sys
input = sys.stdin.readline

n = int(input())

domino = list(tuple(map(int, input().split())) for _ in range(n))

domino.sort(key=lambda x: x[1], reverse=True)
domino.sort(key=lambda x: x[0])

result = 1

for i in range(n-1):
    if domino[i][0] + domino[i][1] < domino[i+1][0]:
        result += 1

print(result)
