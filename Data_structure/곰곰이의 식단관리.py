import sys
input = sys.stdin.readline

n = int(input())

diet = list(input().rstrip())

Chick = 0
NotChick = 1

for meal in diet:
    if meal == 'C':
        Chick += 1
    else:
        NotChick += 1

result = Chick // NotChick

if Chick % NotChick != 0:  # 나누어 떨어지면
    result = Chick // NotChick + 1

print(result)
