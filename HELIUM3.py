# cook your dish here
t=int(input())
for _ in range(t):
    a,b,x,y=map(int, input().split())
    moonpower=a*b
    hpower=x*y
    if hpower >=moonpower:
        print("Yes")
    else:
        print("No")