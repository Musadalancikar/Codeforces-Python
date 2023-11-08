def to_my_critics(a,b,c):
    if a + b >= 10 or a + c >= 10 or b + c >= 10:
        return "YES"
    else:
        return "NO"
    
t = int(input())
total = []

for i in range(t):
    a, b, c = list(map(int, input().split()))
    total.append(to_my_critics(a, b, c))

for j in total:
    print(j)