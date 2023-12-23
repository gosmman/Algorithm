T = int(input())
x = 1
for i in range(T):
    A,B = map(int,input().split())
    print(f"Case #{x}: {A} + {B} = {A+B}")
    x = x+1