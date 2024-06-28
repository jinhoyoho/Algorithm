import sys
input = sys.stdin.readline


n = int(input())

dp = [0 for _ in range(n+1)]
dp[1] = 0

result = [[] for _ in range(n+1)]
result[1].append(1)


for i in range(2, n+1):  # 3부터 시작 -> next는 4부터
    count = dp[i-1] + 1  # 뺄셈인 경우

    result[i] = result[i-1][:]

    if i % 3 == 0:  # 3으로 나누어 떨어진다면
        divide_3 = dp[i//3] + 1
        if count > divide_3:  # 더 작은 경우
            count = divide_3
            result[i] = result[i//3][:]

    if i % 2 == 0:
        divide_2 = dp[i//2] + 1
        if count > divide_2:  # 더 작은 경우
            count = divide_2
            result[i] = result[i//2][:]

    result[i].append(i)

    dp[i] = count

result[n].sort(reverse=True)

print(dp[n])

for num in result[n]:
    print(num, end=' ')
