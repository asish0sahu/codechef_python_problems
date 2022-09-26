# cook your dish here
t=int(input())
for _ in range (t):
    a,b=map(int, input().split())
    p=a/10
    q=b/20
    
    if p>q:
        print("First")
    elif p<q:
        print("Second")
    else:
        print("Any")