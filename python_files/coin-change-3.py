def change(n,pos):
    if n==0: 
        return 1
    if pos==len(coins):
        return 0
    if (n,pos) in memo:
        return memo[(n,pos)]
    #take one more current coin
    memo[(n,pos)]=change(n,pos+1) 
    if(n>=coins[pos]):
        memo[(n,pos)]+=change(n-coins[pos], pos)
    return memo[(n,pos)]

c=int(input())
coins=[int(a) for a in input().split()]
memo={}
n=int(input())
print(change(n,0))