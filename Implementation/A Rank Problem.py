import sys
input = sys.stdin.readline

n, m = map(int, input().split())

rank = list()
for i in range(n):
    rank.append(f'T{i+1}')


for i in range(m):
    first, second = input().split()
    first_index = rank.index(first)
    second_index = rank.index(second)

    if first_index > second_index:  # 더 뒤에 있는 경우
        rank.insert(first_index+1, rank[second_index])
        del rank[second_index]


for team in rank:
    print(team, end=' ')
