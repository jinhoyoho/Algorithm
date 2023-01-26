import sys
input = sys.stdin.readline

n = int(input()) #개수
result = 0
for i in [*sorted(map(int, input().split()))]:
    if result + 1 < i : break
    result += i

print(result+1)