n1,n2=map(int, input().split())

if (n1 >= 1 and n1 <= 9) and (n2 >= 1 and n2 <= 9):
    print(n1*n2)
else:
    print(-1)
