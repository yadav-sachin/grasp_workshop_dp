n=int(input())
table=[0]*(n+1)
table[1]=1
table[2]=2
for i in range(3,n+1):
    table[n]=table[n-1] + table[n-2]