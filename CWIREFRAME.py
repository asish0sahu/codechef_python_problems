# cook your dish here
t=int(input())
for _ in range(t):
    n,m,x=map(int, input().split())
    print(x*(2*n+2*m))