# cook your dish here
t=int(input())
for _ in range(t):
    n,m,k=map(int, input().split())
    print ('Yes' if k*m >= n else 'No')