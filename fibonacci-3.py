def fib(n):
    if n<=2:
        return 1
    if n in memo:                     #check if already solved
        return memo[n]      
    memo[n]=fib(n-1) + fib(n-2)       #store the result before returning
    return memo[n]

memo = {}
n=int(input())
print(fib(n))