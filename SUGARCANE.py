# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    income=n*50
    profit=income-((n*10)+(n*10)+(n*15))
    print(profit)