# cook your dish here
t=int(input())
for _ in range(t):
    n,x=map(int, input().split())
    if n>=x:
        if (n-x)%4 !=0:
            print((n-x)//4+1)
        else:
            print(int((n-x)/4))
    else:
        print("0")
        
