import sys
input = sys.stdin.readline

n, s = map(int, input().split()) #길이n, 원하는 합 s
num_array = list(map(int, input().split())) #수열 입력
result = 987654321 #결과
start, end, sum = 0, 0, 0 #시작, 끝, 합

while True:
    if sum >= s: #합이 크다면
        result = min(result, end - start) 
        sum -= num_array[start]
        start += 1
    
    elif end == n: #끝이면
        break

    else: #s가 더 작다면
        sum += num_array[end]
        end += 1

if result == 987654321:
    print(0)
else:
    print(result)