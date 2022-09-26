# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int, input().split())
    p=x+200
    if y>=x and y<=p:
        print("Yes")
    else:
        print("No")