N = list(map(int,input().split()))
M = [1,1,2,2,2,8]

for i in range(6):
    print(M[i]-N[i], end=' ')