n=int(input())
arr=list(map(int,input().split()))
s=0
for i in range(0,n):
    #tek olmagini yoxlamaq
    if arr[i] % 2 != 0:
        #tekdir.
        continue
    else:
        if n-1 != i:
            if arr[i+1] %2 != 0:
                #ondan sonraki tekdir
                s+=1
                arr[i], arr[i+1] = arr[i+1], arr[i]
print(s)
