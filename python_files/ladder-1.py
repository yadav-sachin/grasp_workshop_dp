def steps(n):
    if n==1: 
        return 1
    if n==2:
        return 2
    return steps(n-1)+steps(n-2)

n=int(input())
print(steps(n))