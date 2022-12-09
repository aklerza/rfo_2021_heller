ededler = [1,2,3,4,5]
arr=list(map(int,input().split()))
for i in ededler:
    if i not in arr:
        print(i)
        break
