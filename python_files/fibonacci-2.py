def fib(n):
    if n<=2:
        return 1
    if (memo[n] != -1):               #check if the problem was already solved
        return memo[n]
    memo[n]=fib(n-1) + fib(n-2)       #store the result before returning
    return memo[n]

max_N=10000
memo=[-1]*max_N
n=int(input())
print(fib(n))