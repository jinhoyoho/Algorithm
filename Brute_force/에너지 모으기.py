import sys
input = sys.stdin.readline

n = int(input()) #구슬의 개수
w = list(map(int, input().split())) #에너지 무게

def backtracking(value):
    global result
    
    if len(w) <= 2:
        result = max(result, value) #둘 중 큰 값 넣기
        return
    
    for i in range(1, len(w)-1): #2번부터 w-1까지 선택
        energy = w[i-1] * w[i+1] #얻은 에너지
        store = w.pop(i) #제거
        backtracking(value + energy) #백트래킹
        w.insert(i, store) #제거한거 다시 넣기
    
result = 0 #결과
backtracking(0) #백트래킹
print(result)