import sys
input = sys.stdin.readline


def dist(point1, point2):
    return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2


case = int(input())

for _ in range(case):
    points = list(tuple(map(int, input().split())) for _ in range(4))  # 점 입력
    result = 0

    points.sort(key=lambda x: (x[1], x[0]))

    dist_list = list()

    for i in range(3):
        for j in range(i+1, 4):
            dist_list.append(dist(points[i], points[j]))

    if len(set(dist_list)) == 2 and dist_list.count(max(dist_list)) == 2 and dist_list.count(min(dist_list)) == 4:
        result = 1

    print(result)
