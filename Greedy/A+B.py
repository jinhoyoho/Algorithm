import sys
input = sys.stdin.readline

count = int(input())

for _ in range(count):
    white_space = input()
    num_string = list(input().rstrip())
    num_int = list()

    for num in num_string:
        num_int.append(int(num))

    num_int.sort(reverse=True)
    first = ''

    for i in range(len(num_int)-1):
        first += str(num_int[i])

    second = num_int[-1]

    print(int(first) + second)
