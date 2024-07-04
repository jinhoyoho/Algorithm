import sys
input = sys.stdin.readline

N = int(input())


for count in range(N):
    n, A, B, C, D, x, y, m = map(int, input().split())

    trees = list()

    X = x
    Y = y

    trees.append((X, Y))

    for i in range(1, n):
        X = (A*X+B) % m
        Y = (C*Y+D) % m

        trees.append((X, Y))

    result = 0

    for i in range(len(trees)-2):
        for j in range(i+1, len(trees)-1):
            for k in range(j+1, len(trees)):

                if ((trees[i][0] + trees[j][0] + trees[k][0])/3).is_integer() and ((trees[i][1] + trees[j][1] + trees[k][1])/3).is_integer():
                    result += 1

    print(f"Case #{count+1}:", result)
