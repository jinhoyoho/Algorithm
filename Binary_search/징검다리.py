import math
import sys
input = sys.stdin.readline

t = int(input()) #테스트 케이스

for _ in range(t): #t번 반복
    n = int(input()) #n입력
    result = int((-1 + int(math.sqrt(1 + 8 * n))) / 2)
    print(result)