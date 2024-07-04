import sys
input = sys.stdin.readline

num = int(input())

score_list = list()

for _ in range(num):
    problem, penalty = map(int, input().split())
    score_list.append((problem, penalty))


score_list.sort(key=lambda x: x[1], reverse=True)
score_list.sort(key=lambda x: x[0], reverse=True)


result = 0

for i in range(5, num):
    if score_list[i][0] == score_list[4][0]:
        result += 1
    else:
        break

print(result)
