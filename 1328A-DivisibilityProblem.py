


n = int(input())

x = []

for i in range(n):
    A, B = list(map(int, input().split()))
    if A % B == 0:
        x.append(0)
    elif A > B:
        blm = A // B
        x.append(((blm+1)*B)-A)
    elif B > A:
        x.append(B-A)
        
for i in x:
    print(i)     
