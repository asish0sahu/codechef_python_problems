# cook your dish here
t= int(input())
for _ in range(t):
    x,y,z=map(int, input().split())
    p=x*5+y*10
    print(int(p/z))