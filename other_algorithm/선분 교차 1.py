import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())  #양 끝점 입력

def ccw(x1,y1,x2,y2,x3,y3): #세 점
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

value1 = ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4) #(x1,y1), (x2,y2)에 대한 직선에 (x3,y3), (x4,y4)대입
value2 = ccw(x3,y3,x4,y4,x1,y1) * ccw(x3,y3,x4,y4,x2,y2) #(x3,y3), (x4,y4)에 대한 직선에 (x1,y1), (x2,y2)대입

if value1 < 0 and value2 < 0: #교점이 있다면
    print(1)
else:
    print(0)