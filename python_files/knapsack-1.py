def knapsack(i,s):
    if i==N:
        return 0
    if wt[i]<=s:
        opt1=val[i] + knapsack(i+1,s-wt[i])
        opt2=knapsack(i+1,s)
        return max(opt1,opt2)
    else:
        return knapsack(i+1,s)

S, N=[int(a) for a in input().split()]
val=[int(a) for a in input().split()]
wt=[int(a) for a in input().split()]
print(knapsack(0,S))