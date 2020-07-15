n=int(input())
a,b=1,1
c=2
if(n<=2):
    print(a)
else:
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
    print(c)