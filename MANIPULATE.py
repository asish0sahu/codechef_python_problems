# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int, input().split())
    if x==y or x>y:
        print("yes")
    else:
        print("no")
        