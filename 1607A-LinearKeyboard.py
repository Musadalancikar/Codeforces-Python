def linear_keybord(n, string):
    total = 0
    if len(string) <= 1:
        return 0
    else:
        start = n.index(string[0])+1
        for j in range(len(string)-1):
            end = n.index(string[j+1])+1
            total += abs(end - start)
            start = end
        return total
    
t = int(input())
result = []

for i in range(t):
    n = input()
    string = input()
    result.append(linear_keybord(n, string))
    
for k in result:
    print(k)