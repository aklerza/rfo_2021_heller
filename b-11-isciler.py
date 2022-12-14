n=int(input())
arr=[0] + list(map(int, input().split()))

dict={}
s=[0]*n

for ind, val in enumerate(arr):
    if val in dict:
        dict[val] += [ind]
    else:
        dict[val] = [ind]
svy=0

for i in range(n):
    if i+1 in dict:
        s[dict[i][0]] = len(dict[i+1])
    
print(" ".join(str(val) for val in s))
