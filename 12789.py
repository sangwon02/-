import sys
input = sys.stdin.readline

n = int(input())
students = list(map(int, input().split())) 

stack = []
now = 1

for student in students:
    stack.append(student)
    while stack and stack[-1] == now:
        stack.pop()
        now +=1

if stack: 
    print('Sad') 
else:
    print('Nice')