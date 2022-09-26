# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int, input().split())
    p=30*y
    
    if x>p or x==p:
        print("Yes")
    else:
        print("No")

