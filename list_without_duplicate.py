# make a list with user input without duplicate
T=int(input())
for i in range(T):
    K=int(input())
    A=[]
    for i in range(K):
        x=map(int,input().split())
        A.extend(x)
    K=set(A)
    print(K)
    print(len(K))
if len(K)==5:
    print("Yes")
else:
    print("No")