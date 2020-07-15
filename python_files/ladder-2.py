from functools import lru_cache

# memo ={1:1, 2:2}
@lru_cache(maxsize=None)
def steps(n):
    # if n in memo:
        # return memo[n]
    # memo[n]=steps(n-1)+steps(n-2)
    # return memo[n]
    if(n==1):
        return 1
    if(n==2):
        return 2
    return steps(n-1)+steps(n-2)

n=int(input())
print(steps(n))