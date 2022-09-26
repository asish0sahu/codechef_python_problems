# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    temp=(x//y)
    if(x%y)==0:
        print(temp*z)
    else:
        print((temp+1)*z)