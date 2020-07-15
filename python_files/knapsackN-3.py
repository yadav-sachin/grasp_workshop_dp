def knapsack(i,s):
    if i==N:
        return 0
    if (i,s) in memo:
        return memo[(i,s)]
    if wt[i]<=s:
        opt1=val[i] + knapsack(i,s-wt[i])
        opt2=knapsack(i+1,s)
        memo[(i,s)]=max(opt1,opt2)
    else:
        memo[(i,s)]=knapsack(i+1,s)
    return memo[(i,s)]

S, N=[int(a) for a in input().split()]
val=[int(a) for a in input().split()]
wt=[int(a) for a in input().split()]
memo={}
print(knapsack(0,S))