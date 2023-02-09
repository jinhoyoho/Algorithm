import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())  #양 끝점 입력

def ccw(x1,y1,x2,y2,x3,y3): #세 점
    value = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if value > 0:
        return 1
    elif value == 0:
        return 0
    else:
        return -1
result = 0
token = 0
if ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4) == 0 and ccw(x3,y3,x4,y4,x1,y1) * ccw(x3,y3,x4,y4,x2,y2) == 0:
    token = 1
    if min(x1,x2)<=max(x3,x4) and min(x3,x4)<=max(x1,x2) and min(y1,y2)<=max(y3,y4) and min(y3,y4)<=max(y1,y2):
        result=1

if ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4)<=0 and ccw(x3,y3,x4,y4,x1,y1) * ccw(x3,y3,x4,y4,x2,y2)<=0:
    if not token:
        result=1

print(result)