# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    count=0
    for i in arr:
        if i>=1000:
            count+=1
    
    print(count)        
            
        
