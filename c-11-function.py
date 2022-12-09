n=abs(int(input()))
s=1
while n > 1:
    if n >= 2:
        s*=n
        n -= 2
s = str(s)
print(len(s) - len(s.rstrip('0')))
