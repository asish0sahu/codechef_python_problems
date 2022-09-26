# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c,d=map(int, input().split())
    p=(a-c)
    q=(b-d)
    
    if p<q:
        print("First")
    elif p>q:
        print("Second")
    else:
        print("Any")
        