n1,n2=map(int,input().split())
m=[]
for i in range(1,n1+1):
    if n1 % i == 0:
        m.append(i)
        
if n2 <= len(m):
    print(m[n2-1])
else:
    print(-1)
