# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c=map(int, input().split())
    sec1=a
    sec2=b
    sec3=c
    
    if a+b+c>=100 and (sec1>=10 and sec2>=10 and sec3>=10):
        print("pass")
    else:
        print("fail")