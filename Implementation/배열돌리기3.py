import sys
input = sys.stdin.readline
#n:행, m:열
n, m, r = map(int, input().split()) #nxm 배열 연산 r번 적용

matrix = list(list(map(int, input().split())) for _ in range(n)) #배열 입력
case_list = list(map(int, input().split())) #연산 횟수

def case1(matrix, row, column): #상하반전
    array = [[0] * column for _ in range(row)] #nxm 배열 생성
    for i in range(row):
        array[i] = matrix[row-1-i][:]

    return array

def case2(matrix, row, column):
    array = [[0] * column for _ in range(row)] #nxm 배열 생성
    for i in range(row):
        data_list = list(matrix[i][:])
        data_list.reverse()
        array[i] = data_list

    return array

#n:행, m:열로 변경
def case3(matrix, row, column):
    array = [[0] * column for _ in range(row)] #mxn 배열 생성
    for j in range(row):
        for i in range(column):
            array[j][i] = matrix[i][j]
    
    for i in range(row):
        array[i].reverse()
    
    return array

#n:열, m:행으로 변경
def case4(matrix, row, column):
    array = [[0] * column for _ in range(row)] #mxn 배열 생성
    for j in range(row-1, -1, -1):
        for i in range(column): 
            array[row - j - 1][i] = matrix[i][j]
    
    return array

def case5(matrix, row, column):
    array = [[0] * column for _ in range(row)] #nxm 배열 생성
    array_1 = [[0] * int(column//2) for _ in range(int(row//2))]
    array_2 = [[0] * int(column//2) for _ in range(int(row//2))]
    array_3 = [[0] * int(column//2) for _ in range(int(row//2))]
    array_4 = [[0] * int(column//2) for _ in range(int(row//2))]
   
    #1번구역 저장
    for i in range(row//2):
        for j in range(column//2):
            array_1[i][j] = matrix[i][j]
    #2번구역 저장
    for i in range(row//2):
        for j in range(column//2):
            array_2[i][j] =  matrix[i][j+column//2]
    #4번구역 저장
    for i in range(row//2):
        for j in range(column//2):
            array_4[i][j] = matrix[i+row//2][j]
    #3번구역 저장
    for i in range(row//2):
        for j in range(column//2):
            array_3[i][j] = matrix[i+row//2][j+column//2]
    
    for i in range(row//2):
        array[i] = array_4[i] + array_1[i]
    for i in range(row//2):
        array[i + row//2] = array_3[i] + array_2[i]

    return array

def case6(matrix, row, column):
    array = [[0] * column for _ in range(row)] #nxm 배열 생성
    array_1 = [[0] * int(column//2) for _ in range(int(row//2))]
    array_2 = [[0] * int(column//2) for _ in range(int(row//2))]
    array_3 = [[0] * int(column//2) for _ in range(int(row//2))]
    array_4 = [[0] * int(column//2) for _ in range(int(row//2))]
   
    #1번구역 저장
    for i in range(row//2):
        for j in range(column//2):
            array_1[i][j] = matrix[i][j]
    #2번구역 저장
    for i in range(row//2):
        for j in range(column//2):
            array_2[i][j] =  matrix[i][j+column//2]
    #4번구역 저장
    for i in range(row//2):
        for j in range(column//2):
            array_4[i][j] = matrix[i+row//2][j]
    #3번구역 저장
    for i in range(row//2):
        for j in range(column//2):
            array_3[i][j] = matrix[i+row//2][j+column//2]
    
    for i in range(row//2):
        array[i] = array_2[i] + array_3[i]
    for i in range(row//2):
        array[i + row//2] = array_1[i] + array_4[i]

    return array


result = matrix
for case in case_list:
    if case == 1:
        result = case1(result, n, m)
    elif case == 2:
        result = case2(result, n, m)
    elif case == 3:
        n, m = m, n
        result = case3(result, n, m) #row, column 변경
    elif case == 4:
        n, m = m, n
        result = case4(result, n, m) #row, column 변경
    elif case == 5:
        result = case5(result, n, m)
    else:
        result = case6(result, n, m)

for i in range(n):
    print(*result[i])