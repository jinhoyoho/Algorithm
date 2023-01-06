import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split())) #배열 저장

dp = [[0] * n for _ in range(2)]
dp[0][0] = num[0]

if n > 1:
    result = -1e9
    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1] + num[i], num[i]) #원소를 제거하지 않았을 때
        dp[1][i] = max(dp[0][i-1], dp[1][i-1] + num[i])#i번째 수를 제거하는 경우, 이미 제거해서 i번째 원소를 선택해야 하는 경우
        result = max(result, dp[0][i], dp[1][i])
    print(result)
else:
    print(num[0])