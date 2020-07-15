arr=[int(a) for a in input().split()]
N=len(arr)
table=[1]*N
for i in range(1,N):
    for j in range(0,i):
        if arr[j]<arr[i]:
            table[i]=max(table[i],table[j]+1)
print(max(table))