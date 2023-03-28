n,m = map(int,input().split())
for z in range (n,m*n+1):
    if z % n == 0:
        print(z)
