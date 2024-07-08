import sys
input = sys.stdin.readline

n = int(input())
num = input().rstrip()  # 메모리 한계로 인해 문자열로 받기

result = 0

for i in range(n):
    result += int(num[i])

print(result)
