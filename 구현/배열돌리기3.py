import sys
input = sys.stdin.readline

n, m, r = map(int, input().split()) #nxm 배열 연산 r번 적용

matrix = list(list(map(int, input().split())) for _ in range(n)) #배열 입력
switch = int(input())

def case1(matrix): #상하반전
    array = [[0] * m for _ in range(n)] #nxm 배열 생성
    for i in range(n):
        array[i] = matrix[n-1-i][:]
    return array

def case2(matrix):
    array = [[0] * m for _ in range(n)] #nxm 배열 생성
    for i in range(n):
        data_list = list(matrix[i][:])
        data_list.reverse()
        array[i] = data_list
    print(array)

def case3(matrix):
    array = [[0] * n for _ in range(m)] #mxn 배열 생성
    for i in range()

case3(matrix)