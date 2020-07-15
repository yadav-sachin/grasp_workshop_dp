def change(n,pos):
    if n==0: 
        return 1
    if pos==len(coins):
        return 0
    #take one more current coin
    if(n>=coins[pos]):
        return change(n-coins[pos], pos) + change(n, pos+1)   
    return change(n,pos+1) 

coins=[1,2,5]
n=int(input())
print(change(n,0))

