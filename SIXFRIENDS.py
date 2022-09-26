# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int, input().split())
    print(min((3*x),(2*y)))