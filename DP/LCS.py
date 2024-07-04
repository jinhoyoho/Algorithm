import sys
input = sys.stdin.readline

first_string = list(input())
second_string = list(input())

dp = [[0] * (len(second_string)) for _ in range(len(first_string))]


for i in range(1, len(first_string)):
    for j in range(1, len(second_string)):
        if first_string[i] == second_string[j]:  # 같다면
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
