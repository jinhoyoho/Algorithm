import sys
input = sys.stdin.readline

n = int(input()) #탑의 개수
tower = list(map(int, input().split())) #탑의 높이
result = [0] * n #탑의 번호를 저장할 리스트
stack = list() #탑의 (높이, 번호)를 저장할 큐
stack.append((tower[0], 1)) #첫 번째 타워의 (높이, 번호)저장

for i in range(1, n): #1~n번까지
    while stack: #빌 때 까지
        if stack[-1][0] > tower[i]: #송신가능하다면
            result[i] = stack[-1][1] #번호 저장
            break
        else:
            stack.pop() #버리기
    
    stack.append((tower[i], i+1)) #(높이, 번호) 저장

print(*result)