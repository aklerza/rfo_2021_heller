a=int(input())
m=[]
for i in range(1,10):
    if a % i == 0:
        m.append(i)

dayandi = False
        
for i in range(0,len(m)-1):
    if not dayandi:
        for k in range(0,len(m)-1):
            if m[i] * m[-k] == a:
                print("Yes")
                dayandi = not dayandi
                break
if not dayandi:
    print("No")
