import sys
input = sys.stdin.readline

t = int(input()) 
count = 0
for _ in range(t): #t번 반복
    word = list(input().rstrip())
    stack = [word[0]]
    for i in range(1, len(word)):
        if stack: #stack이 있다면
            if stack[-1] == word[i]: #마지막이 같다면
                stack.pop()
            else:
                stack.append(word[i])
        else: #비어있다면
            stack.append(word[i])
    
    if not stack:
        count += 1
    

print(count)