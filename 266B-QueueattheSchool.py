
n, t = list(map(int, input().split()))

s = list(input())

for i in range(t):
    x = 0
    while x < n -1:
        if s[x] == "B" and s[x+1] == "G":
            s[x], s[x+1] = s[x+1], s[x]
            x += 2
        else:
            x += 1
            
print("".join(s))
        

