

n = list(input())

total = []
x = 0

while x <= len(n)-1:
    if n[x] == ".":
        total.append(0)
        x += 1
    elif n[x] == "-" and n[x+1] == ".":
        total.append(1)
        x += 2
    elif n[x] == "-" and n[x+1] == "-":
        total.append(2)
        x += 2

print("".join(map(str, total)))
    
    