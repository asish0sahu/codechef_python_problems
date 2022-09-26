# cook your dish here
t=int(input())
for _ in range(t):
    print('In' if sum(map(int, input().split()))==0 else 'out')

#    