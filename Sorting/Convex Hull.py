import sys

input = sys.stdin.readline

n = int(input())
dots = []

for _ in range(n):  #n개 담기
    x, y, c = input().split()
    if c == 'Y':  #껍질을 이루는 점이라면
        dots.append([int(x), int(y)])


def ccw(p1, p2, p3):
    return p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] -
                                                                        p2[1])


dots.sort()  #점 오름차순 정렬
lower = []  #아래 껍질 stack
#ccw 방향으로 stack에 삽입
for d in dots:
    while len(lower) >= 2 and ccw(lower[-2], lower[-1], d) < 0:
        lower.pop()
    lower.append(d)

upper = []  #위 껍질 stack
for d in reversed(dots):  #뒤집어서 ccw방향으로 stack에 삽입
    while len(upper) >= 2 and ccw(upper[-2], upper[-1], d) < 0:
        upper.pop()
    upper.append(d)

result = lower[:-1] + upper[:-1]

print(len(result))
for x, y in result:
    print(x, y)