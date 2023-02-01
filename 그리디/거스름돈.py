import sys
input = sys.stdin.readline

coins = [500, 100, 50, 10, 5]
n = int(input())
n = 1000 - n
result = 0
for coin in coins:
    result += (n // coin) #나눈만큼 저장
    n = n % coin 

result += n #1원짜리 저장
print(result)