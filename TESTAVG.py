# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c=map(int, input().split())
    f=(a+b)/2
    s=(a+c)/2
    m=(b+c)/2
    if f>=35 and s>=35 and m>=35:
        print("Pass")
    else:
        print("Fail")