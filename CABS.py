# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int, input().split())
    if (x<y):
        print("First")
    elif x==y:
        print("Any")
    else:
        print("second")