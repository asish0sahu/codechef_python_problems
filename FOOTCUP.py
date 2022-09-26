# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int, input().split())
    if x==y and x>0:
        print('Yes')
    else:
        print('No')