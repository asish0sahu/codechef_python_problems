# cook your dish here
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    print(min((7-a),(7-b)))