import sys
input = sys.stdin.readline

N = int(input())

result = list()

for _ in range(N-1):
    result.append(1)
    result.append(-1)

result.append(-1)
result.append(1)

print(*result)
