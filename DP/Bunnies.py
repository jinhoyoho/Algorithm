import sys
input = sys.stdin.readline

count = int(input())

dp = [0 for _ in range(46)]

dp[0] = 1
dp[1] = 1

for i in range(2, 46):
    dp[i] = dp[i-1] + dp[i-2]

for _ in range(count):
    num = int(input())
    print(dp[num])
