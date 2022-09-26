# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int, input().split())
    
    if z%x==0 and z%y==0:
        print("Any")
    elif z%x==0:
        print("Chicken")
    elif z%y==0:
        print("Duck")
    elif z%x!=0 and z%y!=0:
        print("None")