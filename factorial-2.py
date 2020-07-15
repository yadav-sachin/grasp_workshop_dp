def fact(n):
    if n==1: 
        return 1
    if n in memo:
        return memo[n]
    memo[n]=n*fact(n-1)
    return memo[n]

memo={}
n=int(input())
print(fact(n))